import os
import subprocess
import shutil
import sys

# ----------------------- PATHS -----------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JUDGE_DIR = os.path.join(BASE_DIR, "..", "judge")

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
    print("❌ No problem folder found. Run 'cfjudge' first!")
    exit(1)

problem_folders.sort(key=lambda x: os.path.getmtime(x[1]), reverse=True)
problem_name, problem_folder = problem_folders[0]

if not os.path.exists(SOLUTION_FILE):
    print(f"❌ test.py not found")
    exit(1)

# Count test cases
test_count = 0
while os.path.exists(os.path.join(problem_folder, f"input{test_count + 1}.txt")):
    test_count += 1

# Open output.txt for writing ALL results
with open(OUTPUT_TXT, "w", encoding="utf-8") as output_file:
    output_file.write(f"Testing {problem_name} with {test_count} test case(s)\n")
    output_file.write("=" * 60 + "\n\n")
    
    all_passed = True
    
    # Run all test cases
    for i in range(1, test_count + 1):
        input_file = os.path.join(problem_folder, f"input{i}.txt")
        expected_file = os.path.join(problem_folder, f"expected{i}.txt")
        
        # Copy input to judge/input.txt
        shutil.copyfile(input_file, INPUT_TXT)
        
        # Create a temporary output file for this test
        temp_output = os.path.join(JUDGE_DIR, "temp_output.txt")
        if os.path.exists(temp_output):
            os.remove(temp_output)
        
        # Temporarily redirect to temp file
        original_stdout = sys.stdout
        with open(temp_output, "w", encoding="utf-8") as temp_out:
            # Run the solution (it will write to temp_output.txt via setup_io)
            result = subprocess.run(
                ["python", SOLUTION_FILE],
                cwd=BASE_DIR,
                capture_output=True,
                text=True
            )
        
        # Check if temp output was created
        if not os.path.exists(temp_output):
            output_file.write(f"❌ Test {i}: No output produced\n\n")
            all_passed = False
            continue
        
        # Read actual output
        with open(temp_output, "r", encoding="utf-8") as f:
            actual = f.read()
        
        # Read expected output
        with open(expected_file, "r", encoding="utf-8") as f:
            expected = f.read()
        
        # Write test result to output.txt
        output_file.write(f"Test {i}:\n")
        output_file.write(f"Input:\n{open(input_file).read()}\n")
        
        # Compare
        if normalize(actual) == normalize(expected):
            output_file.write(f"✅ PASSED\n")
            output_file.write(f"Output:\n{actual}\n")
        else:
            output_file.write(f"❌ FAILED\n")
            output_file.write(f"Expected:\n{expected}\n")
            output_file.write(f"Got:\n{actual}\n")
            all_passed = False
        
        output_file.write("-" * 60 + "\n\n")
        
        # Clean up temp file
        if os.path.exists(temp_output):
            os.remove(temp_output)
    
    output_file.write("=" * 60 + "\n")
    if all_passed:
        output_file.write("🎉 ALL TESTS PASSED!\n")
    else:
        output_file.write("💥 SOME TESTS FAILED\n")

print(f"✅ Results written to: {OUTPUT_TXT}")
print("💡 Open output.txt to see all test results!")