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
    a = [(int(x)) for x in input().split()]
    b,c=[],[]
    mx = max(a)
    for value in a:
        if value != mx:
            b.append(value)
        else:
            c.append(value)
    if len(b) == 0:
        print(-1)
    else:
        print(len(b),len(c))
        print(*b)
        print(*c)
# ================== SOLUTION END ==================

if LOCAL:
    sys.stdout.flush()
#cfjudge
#python run.py
