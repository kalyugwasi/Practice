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
    first, second = str1().split(" ")
    first = list(first)
    n,m = len(first),len(second)
    freq = Counter(second)
    for i in range(n-1,-1,-1):
        ch = first[i]
        if freq[ch]:
            freq[ch] -= 1
        else:
            first[i] = "."
    res = "".join(first).replace(".", "")

    if res == second:
        print("YES")
    else:
        print("NO")

# ================== SOLUTION END ==================

if LOCAL:
    sys.stdout.flush()
#cfjudge
#python run.py