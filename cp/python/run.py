import os
import subprocess
import shutil
import sys

# ----------------------- PATHS -----------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JUDGE_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "judge"))

SOLUTION_FILE = os.path.join(BASE_DIR, "test.py")
INPUT_TXT = os.path.join(JUDGE_DIR, "input.txt")
OUTPUT_TXT = os.path.join(JUDGE_DIR, "output.txt")
# ----------------------------------------------------

def normalize(s):
    """Normalize whitespace for comparison"""
    return s.split()

# Find the most recent problem folder
problem_folders = []
for folder_name in os.listdir(JUDGE_DIR):
    folder_path = os.path.join(JUDGE_DIR, folder_name)
    if os.path.isdir(folder_path) and folder_name not in ["__pycache__"]:
        if os.path.exists(os.path.join(folder_path, "input1.txt")):
            problem_folders.append((folder_name, folder_path))

if not problem_folders:
    exit(1)

problem_folders.sort(key=lambda x: os.path.getmtime(x[1]), reverse=True)
problem_name, problem_folder = problem_folders[0]

if not os.path.exists(SOLUTION_FILE):
    exit(1)

test_count = 0
while os.path.exists(os.path.join(problem_folder, f"input{test_count + 1}.txt")):
    test_count += 1

results_log = []
results_log.append(f"Testing {problem_name} with {test_count} test case(s)")
results_log.append("=" * 60 + "\n")

all_passed = True

for i in range(1, test_count + 1):
    input_file = os.path.join(problem_folder, f"input{i}.txt")
    expected_file = os.path.join(problem_folder, f"expected{i}.txt")
    
    shutil.copyfile(input_file, INPUT_TXT)
    
    # Run the solution silently (redirect stdout/stderr to DEVNULL)
    subprocess.run(
        [sys.executable, SOLUTION_FILE], 
        cwd=BASE_DIR,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    
    actual = ""
    if os.path.exists(OUTPUT_TXT):
        with open(OUTPUT_TXT, "r", encoding="utf-8") as f:
            actual = f.read()
    
    with open(expected_file, "r", encoding="utf-8") as f:
        expected = f.read()
    
    results_log.append(f"Test {i}:")
    results_log.append(actual)
    
    if normalize(actual) == normalize(expected):
        results_log.append(f"✅ PASSED")
    else:
        results_log.append(f"❌ FAILED")
        results_log.append(f"Expected:\n{expected}")
        all_passed = False
    
    results_log.append("-" * 60 + "\n")

results_log.append("=" * 60)
if all_passed:
    results_log.append("🎉 ALL TESTS PASSED!")
else:
    results_log.append("💥 SOME TESTS FAILED")

final_output = "\n".join(results_log)

with open(OUTPUT_TXT, "w", encoding="utf-8") as f:
    f.write(final_output)

# All print statements have been removed for a silent terminal experience.