import sys,os
from collections import Counter
def setup_io():
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        judge_dir = os.path.join(base_dir, "..", "judge")

        input_path = os.path.join(judge_dir, "input.txt")
        output_path = os.path.join(judge_dir, "output.txt")

        if os.path.exists(input_path):
            sys.stdin = open(input_path, "r")
            sys.stdout = open(output_path, "w")
            return True
    except:
        pass

    return False
LOCAL = setup_io()
input = sys.stdin.readline
int1 = lambda: int(input())
str1 = lambda: input().strip()
def inp(): return map(int, input().split())
def ints(): return list(map(int, input().split()))
def strs(): return list(map(str,str1()))

# ================== SOLUTION START ==================

t = int1()
for _ in range(t):
    n = int1()
    a = ints()
    a.sort()

    m = 1
    cur = 1
    for i in range(1, n):
        if a[i] == a[i-1]:
            cur += 1
            if cur > m:
                m = cur
        else:
            cur = 1
    ops = 0
    while (m<n):
        ops += 1
        add = min(m,n-m)
        ops += add
        m += add
    print(ops)

# ================== SOLUTION END ==================

if LOCAL:
    sys.stdout.flush()
#cfjudge
#python run.py