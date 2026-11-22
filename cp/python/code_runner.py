#!/usr/bin/env python3
"""Route Code Runner's test.py shortcut through the local CP checker."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


PYTHON_DIR = Path(__file__).resolve().parent
SCRIPT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else PYTHON_DIR / "test.py"

if SCRIPT == PYTHON_DIR / "test.py":
    command = [sys.executable, str(PYTHON_DIR / "run.py"), "--local"]
    working_directory = PYTHON_DIR
else:
    command = [sys.executable, "-u", str(SCRIPT), *sys.argv[2:]]
    working_directory = Path.cwd()

result = subprocess.run(command, cwd=working_directory)
raise SystemExit(result.returncode)
