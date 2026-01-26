import subprocess

# Run your solution with input.txt
with open("input.txt", "r") as fin:
    result = subprocess.run(
        ["python", "solution.py"],
        stdin=fin,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

# Read expected output
with open("output.txt", "r") as f:
    expected = f.read().strip()

# Get actual output
actual = result.stdout.strip()

# Compare
if actual == expected:
    print("✅ Correct Answer")
else:
    print("❌ Wrong Answer")
    print("\n--- Expected ---")
    print(expected)
    print("\n--- Got ---")
    print(actual)
