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
int1 = lambda: int(input()) #for reading a single number
str1 = lambda: input().strip() #for spliting a char in parts
ints1 = lambda: list(map(int,str1())) #mostly for 0,1
def inp(): return map(int, input().split()) #mainly for multiple known variables
def ints(): return list(map(int, input().split())) #for numerical lists
def strs(): return list(map(str,str1())) #for string list

# ================== SOLUTION START =================

t = int1()
for _ in range(t):
    n,k,b,s = inp()
    l = k*b
    if s < l or s > l + (k - 1) * n:
        print(-1)
        continue    
    li = [0] * n
    li[0] = l
    s -= l
    i = 0

    while s > 0 and i < n:
        o = min(k - 1, s)
        li[i] += o
        s -= o
        i += 1
    if s > 0:
        print(-1)
    else:
        print(*li)



# ================== SOLUTION END ==================

if LOCAL:
    sys.stdout.flush()
#cfjudge
#python run.py