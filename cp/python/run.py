#!/usr/bin/env python3
"""Run the legacy setup_io() scratch file against saved Codeforces samples."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path


PYTHON_DIR = Path(__file__).resolve().parent
JUDGE_DIR = PYTHON_DIR.parent / "judge"
DEFAULT_SOLUTION = PYTHON_DIR / "test.py"
INPUT_TXT = JUDGE_DIR / "input.txt"
OUTPUT_TXT = JUDGE_DIR / "output.txt"
LOCAL_INPUT = PYTHON_DIR / "input.txt"
LOCAL_EXPECTED = PYTHON_DIR / "expected.txt"
LOCAL_OUTPUT = PYTHON_DIR / "output.txt"


def normalize(value: str) -> list[str]:
    return value.split()


def choose_problem(requested: str | None) -> Path:
    if requested:
        folder = JUDGE_DIR / requested.upper()
        if not (folder / "input1.txt").exists():
            raise ValueError(f"No saved samples for {requested}. Run cpjudge {requested} first.")
        return folder
    candidates = [path for path in JUDGE_DIR.iterdir() if path.is_dir() and (path / "input1.txt").exists()]
    if not candidates:
        raise ValueError("No saved problems. Run cpjudge 1904A first.")
    return max(candidates, key=lambda path: path.stat().st_mtime)


def find_test_count(folder: Path) -> int:
    index = 1
    while (folder / f"input{index}.txt").exists() and (folder / f"expected{index}.txt").exists():
        index += 1
    return index - 1


def run_solution(solution: Path, sample_input: str, timeout: float) -> tuple[str, str, bool]:
    """Use the original template's judge/input.txt and judge/output.txt paths."""
    INPUT_TXT.write_text(sample_input, encoding="utf-8")
    OUTPUT_TXT.unlink(missing_ok=True)
    try:
        result = subprocess.run(
            [sys.executable, str(solution)], text=True, capture_output=True,
            timeout=timeout, cwd=solution.parent,
        )
    except subprocess.TimeoutExpired:
        return "", f"TIME LIMIT EXCEEDED (>{timeout:g}s)", True
    actual = OUTPUT_TXT.read_text(encoding="utf-8") if OUTPUT_TXT.exists() else result.stdout
    details = ""
    if result.returncode:
        details = f"Exit code: {result.returncode}"
    if result.stderr.strip():
        details = f"{details}\nstderr:\n{result.stderr.rstrip()}".strip()
    return actual, details, False


def archive(solution: Path, folder: Path) -> str:
    rating = 1100
    metadata = folder / "meta.json"
    if metadata.exists():
        try:
            rating = str(json.loads(metadata.read_text(encoding="utf-8")).get("rating") or rating)
        except json.JSONDecodeError:
            pass
    destination = PYTHON_DIR / "problems" / rating / f"{folder.name}.py"
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(solution, destination)
    return f"Saved solution (replaced existing file if present): {destination}"


def local_test(solution: Path, timeout: float) -> int:
    if not LOCAL_INPUT.exists() or not LOCAL_EXPECTED.exists():
        raise ValueError("Run cpjudge first; cp/python/input.txt and expected.txt are required.")
    actual, details, timed_out = run_solution(solution, LOCAL_INPUT.read_text(encoding="utf-8"), timeout)
    LOCAL_OUTPUT.write_text(actual, encoding="utf-8")
    expected = LOCAL_EXPECTED.read_text(encoding="utf-8")
    passed = not timed_out and not details and normalize(actual) == normalize(expected)
    print("Local editable test: " + ("PASSED" if passed else "FAILED"))
    if details:
        print(details)
    if not passed and not details:
        print(f"Expected:\n{expected.rstrip()}\nActual:\n{actual.rstrip()}")
    print(f"Actual output saved to {LOCAL_OUTPUT}")
    return 0 if passed else 1


def main() -> int:
    parser = argparse.ArgumentParser(description="Test the CP scratch solution against saved samples.")
    parser.add_argument("problem", nargs="?", help="Saved problem key, e.g. 1904A (defaults to newest)")
    parser.add_argument("--solution", type=Path, default=DEFAULT_SOLUTION, help="Solution file to execute")
    parser.add_argument("--timeout", type=float, default=1.0, help="Seconds allowed per sample")
    parser.add_argument("--local", action="store_true", help="Test editable cp/python/input.txt against expected.txt")
    parser.add_argument("--no-archive", action="store_true", help="Do not archive after all samples pass")
    args = parser.parse_args()
    solution = args.solution.resolve()
    if not solution.is_file():
        parser.error(f"Solution file does not exist: {solution}")
    if args.timeout <= 0:
        parser.error("--timeout must be greater than zero")

    if args.local:
        try:
            return local_test(solution, args.timeout)
        except ValueError as error:
            parser.error(str(error))

    try:
        folder = choose_problem(args.problem)
    except ValueError as error:
        parser.error(str(error))
    count = find_test_count(folder)
    summary = [f"Testing {folder.name}: {count} sample(s)", "=" * 60]
    all_passed = True
    for index in range(1, count + 1):
        sample_input = (folder / f"input{index}.txt").read_text(encoding="utf-8")
        expected = (folder / f"expected{index}.txt").read_text(encoding="utf-8")
        actual, details, timed_out = run_solution(solution, sample_input, args.timeout)
        passed = not timed_out and not details and normalize(actual) == normalize(expected)
        summary.append(f"Sample {index}: {'PASSED' if passed else 'FAILED'}")
        if not passed:
            all_passed = False
            if details:
                summary.append(details)
            else:
                summary.append(f"Expected:\n{expected.rstrip()}\nActual:\n{actual.rstrip()}")
        summary.append("-" * 60)

    summary.append("ALL SAMPLES PASSED" if all_passed else "SOME SAMPLES FAILED")
    report = "\n".join(summary) + "\n"
    OUTPUT_TXT.write_text(report, encoding="utf-8")
    print(report, end="")
    if all_passed and not args.no_archive:
        print(archive(solution, folder))
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
