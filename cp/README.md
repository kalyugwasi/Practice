# Competitive-programming workflow

This restores the local workflow around the original `cp/judge/<problem>/inputN.txt`
and `expectedN.txt` folders. It has no Selenium, Chrome, or third-party Python
dependency.

In a Linux VSCodium terminal opened at the repository root, activate the commands
once per shell:

```bash
source cp/activate.sh
```

Then use:

```bash
cpjudge 1904A       # fetch samples, load input1.txt, and open the scratch files
cp 1904 A           # same command; it also accepts one combined problem ID
cpjudge https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/J
cp                  # prompts for the problem ID
cp run              # test cp/python/test.py against the newest fetched problem
cp run 1904A        # test a specific saved problem
```

`cpjudge` copies the recovered template into `cp/python/test.py` only when that
file does not exist, so fetching another problem cannot erase work in progress.
Use `cpjudge 1904A --reset-solution` when you explicitly want a fresh template,
and `--refresh` when you explicitly want to replace existing samples.

Each fetch also synchronizes the first sample into the Python scratch folder:
`cp/python/input.txt`, `cp/python/expected.txt`, and `cp/python/output.txt`.
`input.txt` and `expected.txt` are yours to edit for custom cases. `output.txt`
starts as the expected sample output and is overwritten with actual output when
you run `cp run --local`. This preserves the original `setup_io()` architecture:
the runner temporarily copies the editable input to `cp/judge/input.txt`, lets
the template write to `cp/judge/output.txt`, then mirrors the actual output back
to `cp/python/output.txt`. `cp run` continues to test every official saved sample.

The runner preserves your `setup_io()` architecture: it copies each official
sample into `cp/judge/input.txt` and checks the output written to
`cp/judge/output.txt`. Output comparison ignores trailing and repeated
whitespace. Every passing run saves the current solution under
`cp/python/problems/<rating>/<problem>.py`, replacing a previously saved
solution for that problem; `unsorted` is used if Codeforces did not expose a
rating.

On Windows, add `cp\bin` to `PATH` (or invoke `cp\bin\cp.bat` / `cpjudge.bat`)
to get the same commands in a VSCodium terminal.
