import os
import subprocess
import shutil
import sys
import threading
import time
sys.stdout.reconfigure(encoding='utf-8')
# ----------------------- PATHS -----------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JUDGE_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "judge"))

SOLUTION_FILE = os.path.join(BASE_DIR, "test.py")
INPUT_TXT = os.path.join(JUDGE_DIR, "input.txt")
OUTPUT_TXT = os.path.join(JUDGE_DIR, "output.txt")
# ----------------------------------------------------

TIME_LIMIT_SECONDS = 1
OUTPUT_SIZE_LIMIT_BYTES = 512 * 1024 * 1024  # 512 MB
MONITOR_INTERVAL_SECONDS = 5

def normalize(s):
    """Normalize whitespace for comparison"""
    return s.split()


def monitor_output(proc, output_path, size_limit, stop_event, kill_reason):
    """
    Background thread: checks output file size every MONITOR_INTERVAL_SECONDS.
    Uses stop_event.wait() instead of time.sleep() so it wakes up instantly
    when the process finishes, with no delay on the main thread.
    """
    while not stop_event.wait(timeout=MONITOR_INTERVAL_SECONDS):
        if os.path.exists(output_path):
            size = os.path.getsize(output_path)
            if size > size_limit:
                kill_reason.append("output_limit")
                proc.kill()
                break


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

    # Clear output file before running
    if os.path.exists(OUTPUT_TXT):
        os.remove(OUTPUT_TXT)

    # Launch solution as a subprocess
    proc = subprocess.Popen(
        [sys.executable, SOLUTION_FILE],
        cwd=BASE_DIR,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    # Start live monitor thread
    stop_event = threading.Event()
    kill_reason = []
    monitor_thread = threading.Thread(
        target=monitor_output,
        args=(proc, OUTPUT_TXT, OUTPUT_SIZE_LIMIT_BYTES, stop_event, kill_reason),
        daemon=True
    )
    monitor_thread.start()

    # Wait for process — returns immediately when done, only blocks up to 2s
    tle = False
    try:
        proc.wait(timeout=TIME_LIMIT_SECONDS)
    except subprocess.TimeoutExpired:
        proc.kill()
        proc.wait()
        tle = True

    # Signal monitor to stop — stop_event.wait() wakes up instantly, no 5s delay
    stop_event.set()
    monitor_thread.join()

    results_log.append(f"Test {i}:")

    if tle:
        results_log.append(f"⏱️ TIME LIMIT EXCEEDED (>{TIME_LIMIT_SECONDS}s)")
        results_log.append(f"❌ FAILED")
        all_passed = False
        results_log.append("-" * 60 + "\n")
        continue

    if kill_reason and kill_reason[0] == "output_limit":
        results_log.append(f"💾 OUTPUT LIMIT EXCEEDED (>{OUTPUT_SIZE_LIMIT_BYTES // (1024 * 1024)}MB) — killed by live monitor")
        results_log.append(f"❌ FAILED")
        all_passed = False
        results_log.append("-" * 60 + "\n")
        continue

    # Safe to read output now
    actual = ""
    if os.path.exists(OUTPUT_TXT):
        with open(OUTPUT_TXT, "r", encoding="utf-8") as f:
            actual = f.read()

    results_log.append(actual)

    with open(expected_file, "r", encoding="utf-8") as f:
        expected = f.read()

    if normalize(actual) == normalize(expected):
        results_log.append(f"✅ PASSED")
    else:
        results_log.append(f"❌ FAILED")
        results_log.append(f"Expected:\n{expected}")
        all_passed = False
        #all_passed = True

    results_log.append("-" * 60 + "\n")

results_log.append("=" * 60)
if all_passed:
    results_log.append("🎉 ALL TESTS PASSED!")
else:
    results_log.append("💥 SOME TESTS FAILED")

final_output = "\n".join(results_log)

with open(OUTPUT_TXT, "w", encoding="utf-8") as f:
    f.write(final_output)

# Archive the code if all tests passed
if all_passed:
    dest_dir = os.path.join(BASE_DIR, "problems", "1200")
    os.makedirs(dest_dir, exist_ok=True)
    dest_file = os.path.join(dest_dir, f"{problem_name}.py")
    shutil.copyfile(SOLUTION_FILE, dest_file)
    print(f"✅ Solution archived to {dest_file}")