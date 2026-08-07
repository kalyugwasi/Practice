#!/usr/bin/env python3
"""Fetch competitive-programming samples (Codeforces, AtCoder, CodeChef,
HackerRank) and prepare the local CP scratch file."""

from __future__ import annotations

import argparse
import gzip
import html
import json
import re
import shutil
import subprocess
import sys
import zlib
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[2]
JUDGE_DIR = Path(__file__).resolve().parent
PYTHON_DIR = ROOT / "cp" / "python"
SOLUTION_FILE = PYTHON_DIR / "test.py"
TEMPLATE_FILE = PYTHON_DIR / "template.py"

USER_AGENT = "Mozilla/5.0 (CP local judge)"


@dataclass(frozen=True)
class ProblemRef:
    judge: str  # "codeforces" | "atcoder" | "codechef" | "hackerrank"
    contest: str
    letter: str
    url: str
    group: str | None = None

    @property
    def key(self) -> str:
        if self.judge == "codeforces":
            return f"{self.contest}{self.letter}"
        prefix = {"atcoder": "AT", "codechef": "CC", "hackerrank": "HR"}[self.judge]
        return f"{prefix}_{self.contest}_{self.letter}"


# ---------------------------------------------------------------------------
# Codeforces sample parsing
# ---------------------------------------------------------------------------


class CodeforcesSampleParser(HTMLParser):
    """Extract the contents of Codeforces' sample input/output <pre> blocks."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.section: str | None = None
        self.div_sections: list[str | None] = []
        self.in_pre = False
        self.buffer: list[str] = []
        self.inputs: list[str] = []
        self.outputs: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        classes = set((dict(attrs).get("class") or "").split())
        if tag == "div":
            if "input" in classes:
                self.section = "input"
            elif "output" in classes:
                self.section = "output"
            self.div_sections.append(self.section)
        elif tag == "pre" and self.section:
            self.in_pre = True
            self.buffer = []
        elif tag == "br" and self.in_pre:
            self.buffer.append("\n")

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "br" and self.in_pre:
            self.buffer.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if tag == "pre" and self.in_pre:
            # Codeforces often places a formatting newline immediately after
            # <pre>. Remove only outer line breaks, not spaces in test data.
            value = "".join(self.buffer).strip("\r\n") + "\n"
            if self.section == "input":
                self.inputs.append(value)
            else:
                self.outputs.append(value)
            self.in_pre = False
            self.buffer = []
        elif tag == "div":
            if self.div_sections:
                self.div_sections.pop()
            self.section = self.div_sections[-1] if self.div_sections else None

    def handle_data(self, data: str) -> None:
        if self.in_pre:
            self.buffer.append(data)


def extract_cf_rating(html_text: str) -> str | None:
    match = re.search(r'class="tag-box[^"\n]*"[^>]*>\s*(\d{3,4})\s*<', html_text)
    return match.group(1) if match else None


# ---------------------------------------------------------------------------
# AtCoder sample parsing
# ---------------------------------------------------------------------------


def extract_atcoder_samples(html_text: str) -> tuple[list[str], list[str]]:
    """Extract Sample Input/Output blocks from an AtCoder task page.

    AtCoder embeds both the Japanese and English versions of the statement
    in the same HTML (toggled client-side), and the exact wrapper markup
    around each sample has changed over the years. Rather than depend on a
    specific DOM shape (div/span nesting, particular class names, etc.),
    this anchors on the literal English heading text ("Sample Input 1",
    "Sample Output 2", ...) and grabs the next <pre>...</pre> after it. That
    is robust to markup changes and naturally skips the Japanese copies,
    which are headed "入力例"/"出力例" instead.
    """
    inputs: dict[int, str] = {}
    outputs: dict[int, str] = {}
    pattern = re.compile(
        r"Sample\s+(Input|Output)(?:\s|<(?!pre\b)[^>]+>)*(\d+)\b.{0,600}?<pre[^>]*>(.*?)</pre>",
        re.DOTALL | re.IGNORECASE,
    )
    for kind, number, content in pattern.findall(html_text):
        value = _strip_tags(content).strip("\r\n") + "\n"
        target = inputs if kind.lower() == "input" else outputs
        target.setdefault(int(number), value)

    ordered = sorted(set(inputs) & set(outputs))
    return [inputs[n] for n in ordered], [outputs[n] for n in ordered]


# ---------------------------------------------------------------------------
# CodeChef sample parsing
# ---------------------------------------------------------------------------


def _strip_tags(text: str) -> str:
    return html.unescape(re.sub(r"<[^>]+>", "", text))


def extract_codechef_samples(body_html: str) -> tuple[list[str], list[str]]:
    inputs: list[str] = []
    outputs: list[str] = []

    # Classic style: a single <pre> block containing both "Input:" and
    # "Output:" sections.
    for match in re.finditer(r"<pre[^>]*>(.*?)</pre>", body_html, re.DOTALL | re.IGNORECASE):
        block = _strip_tags(match.group(1))
        io_match = re.search(
            r"Input:?\s*\n(.*?)\n\s*Output:?\s*\n(.*)", block, re.DOTALL | re.IGNORECASE
        )
        if io_match:
            inputs.append(io_match.group(1).strip("\r\n") + "\n")
            outputs.append(io_match.group(2).strip("\r\n") + "\n")

    if inputs:
        return inputs, outputs

    # Newer style: separate "Input"/"Output" headings each followed by their
    # own <pre> block.
    pairs = re.findall(
        r"<h[1-4][^>]*>([^<]*)</h[1-4]>\s*<pre[^>]*>(.*?)</pre>",
        body_html,
        re.DOTALL | re.IGNORECASE,
    )
    pending_input: str | None = None
    for heading, content in pairs:
        value = _strip_tags(content).strip("\r\n") + "\n"
        heading_lower = heading.lower()
        if "input" in heading_lower:
            pending_input = value
        elif "output" in heading_lower and pending_input is not None:
            inputs.append(pending_input)
            outputs.append(value)
            pending_input = None

    return inputs, outputs


# ---------------------------------------------------------------------------
# HackerRank sample parsing
# ---------------------------------------------------------------------------


def extract_hackerrank_samples(body_html: str) -> tuple[list[str], list[str]]:
    """Extract Sample Input/Output blocks from a HackerRank challenge's
    body_html (as returned by the /rest/contests/.../challenges/... API).

    HackerRank labels samples "Sample Input 0" / "Sample Output 0" (0-indexed)
    when there are several, or just "Sample Input" / "Sample Output" with no
    number when there's only one. As with AtCoder, we anchor on the literal
    heading text and grab the next <pre> block rather than depending on the
    exact wrapper markup (<h5>, <p>, nested <span>, etc. all show up in the
    wild across different challenges).
    """
    inputs = {}
    outputs = {}

    for kind in ("Input", "Output"):
        for m in re.finditer(rf"Sample\s+{kind}\s*(\d*)", body_html, re.I):
            number = int(m.group(1) or 0)

            pre = re.search(
                r"<pre[^>]*>(.*?)</pre>",
                body_html[m.end():],
                re.S | re.I,
            )

            if not pre:
                continue

            value = _strip_tags(pre.group(1)).strip("\r\n") + "\n"

            if kind == "Input":
                inputs[number] = value
            else:
                outputs[number] = value

    ordered = sorted(inputs.keys() & outputs.keys())
    return [inputs[i] for i in ordered], [outputs[i] for i in ordered]

# ---------------------------------------------------------------------------
# Problem parsing (turns user input into a ProblemRef)
# ---------------------------------------------------------------------------


def _atcoder_from_task_id(task_id: str) -> ProblemRef:
    task_id = task_id.strip().lower().replace("/", "_")
    if "_" not in task_id:
        raise ValueError("AtCoder tasks look like abc300_a (or abc300/a).")
    contest, letter = task_id.rsplit("_", 1)
    return ProblemRef(
        judge="atcoder",
        contest=contest,
        letter=letter.upper(),
        url=f"https://atcoder.jp/contests/{contest}/tasks/{task_id}",
    )


def _codechef_from_code(raw: str) -> ProblemRef:
    raw = raw.strip()
    if "/" in raw:
        contest, code = raw.split("/", 1)
        contest = contest.strip().upper()
        code = code.strip().upper()
        url = f"https://www.codechef.com/{contest}/problems/{code}"
    else:
        contest = "PRACTICE"
        code = raw.upper()
        url = f"https://www.codechef.com/problems/{code}"
    return ProblemRef(judge="codechef", contest=contest, letter=code, url=url)


def _hackerrank_from_slug(raw: str) -> ProblemRef:
    raw = raw.strip().strip("/")
    if "/" in raw:
        contest, slug = raw.split("/", 1)
        contest = contest.strip().lower()
        slug = slug.strip().lower()
        url = f"https://www.hackerrank.com/contests/{contest}/challenges/{slug}"
    else:
        contest = "master"
        slug = raw.lower()
        url = f"https://www.hackerrank.com/challenges/{slug}/problem"
    return ProblemRef(judge="hackerrank", contest=contest, letter=slug, url=url)


def parse_problem(parts: list[str]) -> ProblemRef:
    raw = "".join(parts).strip()

    # Explicit judge prefixes: cf:1904A, at:abc300_a, cc:START123/FLOW001,
    # hr:solve-me-first, hr:contestslug/challenge-slug
    prefix_match = re.match(
        r"(?i)^(cf|codeforces|at|atcoder|cc|codechef|hr|hackerrank):\s*(.+)$", raw
    )
    if prefix_match:
        prefix, rest = prefix_match.groups()
        prefix = prefix.lower()
        if prefix in ("cf", "codeforces"):
            return _parse_codeforces([rest])
        if prefix in ("at", "atcoder"):
            return _atcoder_from_task_id(rest)
        if prefix in ("cc", "codechef"):
            return _codechef_from_code(rest)
        return _hackerrank_from_slug(rest)

    # AtCoder URL: https://atcoder.jp/contests/abc300/tasks/abc300_a
    atcoder_match = re.fullmatch(
        r"https?://atcoder\.jp/contests/([^/]+)/tasks/([^/?#]+)/?", raw, re.IGNORECASE
    )
    if atcoder_match:
        contest, task_id = atcoder_match.groups()
        letter = task_id.rsplit("_", 1)[-1].upper()
        return ProblemRef(
            judge="atcoder",
            contest=contest,
            letter=letter,
            url=f"https://atcoder.jp/contests/{contest}/tasks/{task_id}",
        )

    # CodeChef URL: https://www.codechef.com/problems/CODE
    #            or https://www.codechef.com/CONTEST/problems/CODE
    codechef_match = re.fullmatch(
        r"https?://(?:www\.)?codechef\.com/(?:([A-Za-z0-9]+)/)?problems/([A-Za-z0-9_]+)/?",
        raw,
        re.IGNORECASE,
    )
    if codechef_match:
        contest, code = codechef_match.groups()
        contest = (contest or "PRACTICE").upper()
        code = code.upper()
        return ProblemRef(judge="codechef", contest=contest, letter=code, url=raw)

    # HackerRank URL: https://www.hackerrank.com/challenges/SLUG(/problem)
    #              or https://www.hackerrank.com/contests/CONTEST/challenges/SLUG(/problem)
    hackerrank_contest_match = re.fullmatch(
        r"https?://(?:www\.)?hackerrank\.com/contests/([^/]+)/challenges/([^/?#]+)/?(?:problem/?)?",
        raw,
        re.IGNORECASE,
    )
    if hackerrank_contest_match:
        contest, slug = hackerrank_contest_match.groups()
        return ProblemRef(
            judge="hackerrank", contest=contest.lower(), letter=slug.lower(), url=raw
        )
    hackerrank_match = re.fullmatch(
        r"https?://(?:www\.)?hackerrank\.com/challenges/([^/?#]+)/?(?:problem/?)?",
        raw,
        re.IGNORECASE,
    )
    if hackerrank_match:
        (slug,) = hackerrank_match.groups()
        return ProblemRef(judge="hackerrank", contest="master", letter=slug.lower(), url=raw)

    # Everything else is assumed to be Codeforces (URL or bare id), matching
    # this script's original behaviour.
    return _parse_codeforces([raw])


def _parse_codeforces(parts: list[str]) -> ProblemRef:
    raw = "".join(parts).strip()
    group_match = re.fullmatch(
        r"https?://codeforces\.com/group/([^/]+)/contest/(\d+)/problem/([a-z]\d?)/?", raw, re.IGNORECASE,
    )
    if group_match:
        group, contest, letter = group_match.groups()
        return ProblemRef(
            judge="codeforces",
            contest=contest,
            letter=letter.upper(),
            group=group,
            url=f"https://codeforces.com/group/{group}/contest/{contest}/problem/{letter.upper()}",
        )
    problemset_match = re.fullmatch(
        r"https?://codeforces\.com/(?:problemset/problem|contest)/(\d+)/(?:problem/)?([a-z]\d?)/?", raw, re.IGNORECASE,
    )
    if problemset_match:
        contest, letter = problemset_match.groups()
        return ProblemRef(
            judge="codeforces",
            contest=contest,
            letter=letter.upper(),
            url=f"https://codeforces.com/problemset/problem/{contest}/{letter.upper()}",
        )
    match = re.fullmatch(r"(\d+)([A-Z]\d?)", raw.upper())
    if not match:
        raise ValueError(
            "Use 1904A, atcoder:abc300_a, codechef:FLOW001, hr:solve-me-first, "
            "or paste a Codeforces/AtCoder/CodeChef/HackerRank problem URL."
        )
    contest, letter = match.groups()
    return ProblemRef(
        judge="codeforces",
        contest=contest,
        letter=letter,
        url=f"https://codeforces.com/problemset/problem/{contest}/{letter}",
    )


# ---------------------------------------------------------------------------
# Fetching
# ---------------------------------------------------------------------------


def fetch_url(url: str) -> str:
    request = Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            # Explicitly accept only encodings we know how to decompress below;
            # some CDNs (e.g. the ones fronting AtCoder) compress responses
            # even when the client didn't ask for it.
            "Accept-Encoding": "gzip, deflate",
        },
    )
    try:
        with urlopen(request, timeout=30) as response:
            raw = response.read()
            encoding = (response.headers.get("Content-Encoding") or "").lower()
            if encoding == "gzip":
                raw = gzip.decompress(raw)
            elif encoding == "deflate":
                raw = zlib.decompress(raw)
            charset = response.headers.get_content_charset() or "utf-8"
            return raw.decode(charset, errors="replace")
    except HTTPError as error:
        raise RuntimeError(f"HTTP {error.code} for {url}") from error
    except URLError as error:
        raise RuntimeError(f"Could not reach {url}: {error.reason}") from error


def fetch_json(url: str) -> dict:
    text = fetch_url(url)
    try:
        return json.loads(text)
    except json.JSONDecodeError as error:
        raise RuntimeError(f"Could not parse JSON from {url}: {error}") from error


def get_codeforces_samples(problem: ProblemRef) -> tuple[list[str], list[str], str | None]:
    page = fetch_url(problem.url)
    parser = CodeforcesSampleParser()
    parser.feed(page)
    return parser.inputs, parser.outputs, extract_cf_rating(page)


def get_atcoder_samples(problem: ProblemRef) -> tuple[list[str], list[str], str | None]:
    page = fetch_url(problem.url)
    inputs, outputs = extract_atcoder_samples(page)
    return inputs, outputs, None


def get_codechef_samples(problem: ProblemRef) -> tuple[list[str], list[str], str | None]:
    api_url = f"https://www.codechef.com/api/contests/{problem.contest}/problems/{problem.letter}"
    data = fetch_json(api_url)
    body = data.get("body") or data.get("problem_statement") or ""
    if not body:
        raise RuntimeError("CodeChef response did not include a problem body.")
    inputs, outputs = extract_codechef_samples(body)
    rating = data.get("difficulty_rating") or data.get("problem_rating") or data.get("rating")
    return inputs, outputs, (str(rating) if rating else None)


def get_hackerrank_samples(problem: ProblemRef) -> tuple[list[str], list[str], str | None]:
    api_url = (
        f"https://www.hackerrank.com/rest/contests/{problem.contest}"
        f"/challenges/{problem.letter}"
    )
    data = fetch_json(api_url)
    model = data.get("model") or data
    body = model.get("body_html") or model.get("preview") or ""
    if not body:
        raise RuntimeError("HackerRank response did not include a problem body.")
    inputs, outputs = extract_hackerrank_samples(body)
    rating = model.get("difficulty_name") or model.get("difficulty")
    return inputs, outputs, (str(rating) if rating else None)


JUDGE_FETCHERS = {
    "codeforces": get_codeforces_samples,
    "atcoder": get_atcoder_samples,
    "codechef": get_codechef_samples,
    "hackerrank": get_hackerrank_samples,
}

JUDGE_LABELS = {
    "codeforces": "Codeforces",
    "atcoder": "AtCoder",
    "codechef": "CodeChef",
    "hackerrank": "HackerRank",
}


# ---------------------------------------------------------------------------
# Local file management (judge-agnostic)
# ---------------------------------------------------------------------------


def write_samples(folder: Path, inputs: list[str], outputs: list[str]) -> None:
    for path in list(folder.glob("input*.txt")) + list(folder.glob("expected*.txt")):
        path.unlink()
    for number, (sample_input, sample_output) in enumerate(zip(inputs, outputs), 1):
        (folder / f"input{number}.txt").write_text(sample_input, encoding="utf-8")
        (folder / f"expected{number}.txt").write_text(sample_output, encoding="utf-8")


def ensure_solution(reset: bool) -> None:
    if reset or not SOLUTION_FILE.exists():
        shutil.copyfile(TEMPLATE_FILE, SOLUTION_FILE)
        print(f"Created scratch solution: {SOLUTION_FILE}")
    else:
        print(f"Keeping existing scratch solution: {SOLUTION_FILE}")


def sync_python_files(folder: Path) -> None:
    """Keep editable local input/output copies beside the scratch solution."""
    sample_input = folder / "input1.txt"
    sample_output = folder / "expected1.txt"
    shutil.copyfile(sample_input, PYTHON_DIR / "input.txt")
    shutil.copyfile(sample_output, PYTHON_DIR / "expected.txt")
    # output.txt starts as the sample output, then a direct run of test.py replaces
    # it with the actual output. expected.txt remains available for comparison.
    shutil.copyfile(sample_output, PYTHON_DIR / "output.txt")


def open_in_editor(paths: list[Path]) -> None:
    editor = shutil.which("codium") or shutil.which("code")
    if editor:
        subprocess.Popen([editor, "--reuse-window", *(str(path) for path in paths)])
    else:
        print("No 'codium' or 'code' command found; open the files shown above manually.")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Fetch Codeforces, AtCoder, CodeChef, or HackerRank samples into cp/judge."
    )
    parser.add_argument(
        "problem",
        nargs="*",
        help=(
            "Problem id or URL, e.g. 1904A, atcoder:abc300_a, codechef:FLOW001, "
            "codechef:START123/FLOW001, hr:solve-me-first, or a full problem URL "
            "from any of the four."
        ),
    )
    parser.add_argument("--refresh", action="store_true", help="Replace existing saved samples")
    parser.add_argument("--reset-solution", action="store_true", help="Replace python/test.py with template.py")
    parser.add_argument("--no-open", action="store_true", help="Do not open files in VSCodium/VS Code")
    args = parser.parse_args()

    if args.problem:
        try:
            problem = parse_problem(args.problem)
        except ValueError as error:
            parser.error(str(error))
    else:
        entered = input(
            "Problem id or URL (e.g. 1904A, atcoder:abc300_a, codechef:FLOW001, hr:solve-me-first): "
        ).strip()
        try:
            problem = parse_problem([entered])
        except ValueError as error:
            parser.error(str(error))

    key = problem.key
    folder = JUDGE_DIR / key
    has_samples = (folder / "input1.txt").exists() and (folder / "expected1.txt").exists()
    label = JUDGE_LABELS[problem.judge]

    if has_samples and not args.refresh:
        print(f"Samples already exist in {folder}. Use --refresh to download them again.")
    else:
        print(f"Fetching {label} {key}…")
        try:
            fetcher = JUDGE_FETCHERS[problem.judge]
            inputs, outputs, rating = fetcher(problem)
        except RuntimeError as error:
            print(f"Fetch failed: {error}", file=sys.stderr)
            return 1
        if not inputs or len(inputs) != len(outputs):
            print("Could not find matching sample input/output blocks on the problem page.", file=sys.stderr)
            return 1
        folder.mkdir(parents=True, exist_ok=True)
        write_samples(folder, inputs, outputs)
        metadata = {
            "problem": key,
            "judge": problem.judge,
            "contest": problem.contest,
            "letter": problem.letter,
            "group": problem.group,
            "source_url": problem.url,
            "rating": rating,
        }
        (folder / "meta.json").write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
        print(f"Saved {len(inputs)} sample(s) to {folder}")

    first_input = folder / "input1.txt"
    if not first_input.exists():
        print(f"No samples are available in {folder}.", file=sys.stderr)
        return 1
    shutil.copyfile(first_input, JUDGE_DIR / "input.txt")
    sync_python_files(folder)
    ensure_solution(args.reset_solution)

    print(f"Input:    {first_input}")
    print(f"Expected: {folder / 'expected1.txt'}")
    print(f"Solution: {SOLUTION_FILE}")
    print(f"Editable input:    {PYTHON_DIR / 'input.txt'}")
    print(f"Expected output:   {PYTHON_DIR / 'expected.txt'}")
    print(f"Actual output:     {PYTHON_DIR / 'output.txt'}")
    if not args.no_open:
        open_in_editor([
            SOLUTION_FILE,
            PYTHON_DIR / "input.txt",
            PYTHON_DIR / "expected.txt",
            PYTHON_DIR / "output.txt",
        ])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())