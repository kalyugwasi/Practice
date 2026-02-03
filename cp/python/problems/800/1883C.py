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
    n,k = inp()
    a = ints()
    cnt2 = 0
    mi = float("inf")
    for i in a:
        if i%k==0:
            mi = 0
            break
        elif i%2==0:
            cnt2 += 1
        mi = min(mi,k-(i%k))
    if k ==4:
        if cnt2>=2:
            mi = min(mi,0)
        elif cnt2 == 1:
            mi = min(mi,1)
        elif cnt2 == 0:
            mi = min(mi,2)
    print(mi)
    

# ================== SOLUTION END ==================

if LOCAL:
    sys.stdout.flush()
#cfjudge
#python run.py