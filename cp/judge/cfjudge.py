#!/usr/bin/env python3
"""Fetch Codeforces samples and prepare the local CP scratch file."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
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


@dataclass(frozen=True)
class ProblemRef:
    contest: str
    letter: str
    url: str
    group: str | None = None

    @property
    def key(self) -> str:
        return f"{self.contest}{self.letter}"


class SampleParser(HTMLParser):
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


def parse_problem(parts: list[str]) -> ProblemRef:
    raw = "".join(parts).strip()
    group_match = re.fullmatch(
        r"https?://codeforces\.com/group/([^/]+)/contest/(\d+)/problem/([a-z]\d?)/?", raw, re.IGNORECASE,
    )
    if group_match:
        group, contest, letter = group_match.groups()
        return ProblemRef(
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
            contest=contest,
            letter=letter.upper(),
            url=f"https://codeforces.com/problemset/problem/{contest}/{letter.upper()}",
        )
    match = re.fullmatch(r"(\d+)([A-Z]\d?)", raw.upper())
    if not match:
        raise ValueError("Use 1904A, or paste a Codeforces problem/group URL.")
    contest, letter = match.groups()
    return ProblemRef(
        contest=contest,
        letter=letter,
        url=f"https://codeforces.com/problemset/problem/{contest}/{letter}",
    )


def fetch_page(problem: ProblemRef) -> str:
    request = Request(problem.url, headers={"User-Agent": "Mozilla/5.0 (CP local judge)"})
    try:
        with urlopen(request, timeout=30) as response:
            return response.read().decode("utf-8", errors="replace")
    except HTTPError as error:
        raise RuntimeError(f"Codeforces returned HTTP {error.code} for {problem.url}") from error
    except URLError as error:
        raise RuntimeError(f"Could not reach Codeforces: {error.reason}") from error


def extract_rating(html: str) -> str | None:
    match = re.search(r'class="tag-box[^"\n]*"[^>]*>\s*(\d{3,4})\s*<', html)
    return match.group(1) if match else None


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
    parser = argparse.ArgumentParser(description="Fetch Codeforces samples into cp/judge.")
    parser.add_argument("problem", nargs="*", help="Problem ID (1904A) or a full Codeforces URL")
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
        entered = input("Codeforces problem or URL (for example 1904A): ").strip()
        try:
            problem = parse_problem([entered])
        except ValueError as error:
            parser.error(str(error))

    key = problem.key
    folder = JUDGE_DIR / key
    has_samples = (folder / "input1.txt").exists() and (folder / "expected1.txt").exists()

    if has_samples and not args.refresh:
        print(f"Samples already exist in {folder}. Use --refresh to download them again.")
    else:
        print(f"Fetching Codeforces {key}…")
        try:
            page = fetch_page(problem)
        except RuntimeError as error:
            print(f"Fetch failed: {error}", file=sys.stderr)
            return 1
        samples = SampleParser()
        samples.feed(page)
        if not samples.inputs or len(samples.inputs) != len(samples.outputs):
            print("Could not find matching sample input/output blocks on the Codeforces page.", file=sys.stderr)
            return 1
        folder.mkdir(parents=True, exist_ok=True)
        write_samples(folder, samples.inputs, samples.outputs)
        metadata = {
            "problem": key,
            "contest": problem.contest,
            "letter": problem.letter,
            "group": problem.group,
            "source_url": problem.url,
            "rating": extract_rating(page),
        }
        (folder / "meta.json").write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
        print(f"Saved {len(samples.inputs)} sample(s) to {folder}")

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
