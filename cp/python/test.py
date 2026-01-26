import sys
import os

def setup_io():
    """
    If running locally with judge folder, redirect I/O.
    Otherwise (Codeforces), do nothing.
    """
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        judge_dir = os.path.join(base_dir, "..", "judge")

        input_path = os.path.join(judge_dir, "input.txt")
        output_path = os.path.join(judge_dir, "output.txt")

        if os.path.exists(input_path):
            sys.stdin = open(input_path, "r")
            sys.stdout = open(output_path, "w")
            return True   # local mode
    except:
        pass

    return False          # CF mode


LOCAL = setup_io()
input = sys.stdin.readline

# ================== SOLUTION START ==================

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(sum(a))

# ================== SOLUTION END ==================

if LOCAL:
    sys.stdout.flush()
#python cfjudge.py
#python test.py