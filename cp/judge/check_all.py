import subprocess
import glob

def normalize(s):
    return s.split()

inputs = sorted(glob.glob("input*.txt"))

all_ok = True

for inp in inputs:
    idx = inp.replace("input", "").replace(".txt", "")
    outp = f"output{idx}.txt"

    with open(inp, "r") as fin:
        result = subprocess.run(
            ["python", "solution.py"],
            stdin=fin,
            stdout=subprocess.PIPE,
            text=True
        )

    with open(outp, "r") as f:
        expected = f.read()

    if normalize(result.stdout) == normalize(expected):
        print(f"✅ Test {idx}: OK")
    else:
        print(f"❌ Test {idx}: WA")
        print("Expected:")
        print(expected)
        print("Got:")
        print(result.stdout)
        all_ok = False

if all_ok:
    print("\n🎉 ALL TESTS PASSED")
else:
    print("\n💥 SOME TESTS FAILED")
