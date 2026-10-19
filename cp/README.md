# Competitive-programming workflow

This restores the local workflow around `cp/judge/<problem>/inputN.txt` and
`expectedN.txt`. Sample fetching uses Python's standard library; no Selenium,
Chrome, or third party Python packages are needed.

From a macOS or Linux terminal opened at the repository root, activate the
commands once per shell:

```bash
source cp/activate.sh
```

Then use:

```bash
cpjudge 1904A       # fetch samples and open the scratch files
cp 1904 A           # same fetch command; combined IDs like 1904A also work
cpjudge https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/J
cp                  # prompts for the problem ID
cp run              # test against the most recently changed saved problem
cp run 1904A        # test against a specific saved problem
```

The shorter form `cpjudge 1904A` is usually the easiest way to start. Run
`source cp/activate.sh` again in each new terminal before using `cp` or
`cpjudge`; alternatively call `./cp/bin/cpjudge 1904A` directly.

`cpjudge` copies `cp/python/template.py` into `cp/python/test.py` only when that
file does not exist, so fetching another problem cannot erase work in progress.
Use `cpjudge 1904A --reset-solution` only when you want to replace your scratch
solution with a fresh template, and `--refresh` when you want to replace saved
samples. Fetching an already-saved problem without `--refresh` reuses its saved
samples.

Each fetch also synchronizes the first sample into the Python scratch folder:
`cp/python/input.txt`, `cp/python/expected.txt`, and `cp/python/output.txt`.
`input.txt` and `expected.txt` are yours to edit for custom cases. `output.txt`
starts as the expected sample output and is overwritten with actual output when
you run either `cp run --local` or `cp run [problem]` (for sample runs it holds
the last sample's output). This preserves the original `setup_io()` architecture:
the runner temporarily copies the editable input to `cp/judge/input.txt`, lets
the template write to `cp/judge/output.txt`, then mirrors the actual output back
to `cp/python/output.txt`. `cp run` continues to test every official saved sample.

The runner preserves your `setup_io()` architecture: it copies each official
sample into `cp/judge/input.txt` and checks the output written to
`cp/judge/output.txt`. Output comparison ignores whitespace differences. A run
that passes every sample saves the current solution under
`cp/python/problems/<rating>/<problem>.py`, replacing a previously saved
solution for that problem. `--no-archive` skips this save. The `--local` option
tests your editable `cp/python/input.txt` against `cp/python/expected.txt` and
writes actual output to `cp/python/output.txt`. Official sample runs also save
their last sample's actual output there; the full pass/fail report stays in
`cp/judge/output.txt`.

On Windows, add `cp\bin` to `PATH` (or invoke `cp\bin\cp.bat` /
`cp\bin\cpjudge.bat`) to get the same commands in a VSCodium terminal.
