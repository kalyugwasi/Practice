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
def inp(): return map(int, input().split())
def ints(): return list(map(int, input().split()))
def int1(): return int(input())
def str1(): return input().strip()


# ================== SOLUTION START ==================

t = int1()
for _ in range(t):
    trg,k,x = inp()
    if x!= 1:
        print("YES")
        print(trg)
        print(*[1]*trg)
    else:
        if k==1:
            print("NO")
        else:
            if trg%2==0:
                print("YES")
                print(trg//2)
                print(*[2]*(trg//2))
            else:
                if k>3:
                    print("YES")
                    print((trg-3)//2+1)
                    print(3,*([2]*((n-3)//2)))
                else:
                    print("NO")
        
# ================== SOLUTION END ==================

if LOCAL:
    sys.stdout.flush()
#cfjudge
#python run.py
