import sys,os
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
    ops,ok = 0,True
    for i in range(n-2,-1,-1):
        if a[i] >= a[i+1]:
            if a[i+1] == 0:
                ok = False
                break
            ops_needed = a[i].bit_length() - (a[i+1] - 1).bit_length()
            if ops_needed < 0:
                ops_needed = 0
            if (a[i] >> ops_needed) >= a[i+1]:
                ops_needed += 1
            ops += ops_needed
            a[i] = a[i] >> ops_needed
    print(ops if ok else -1)

# ================== SOLUTION END ==================

if LOCAL:
    sys.stdout.flush()
#cfjudge
#python run.py