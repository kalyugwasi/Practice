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
dx = [-1,1,-1,1]
dy = [-1,-1,1,1]
for _ in range(t):
    a,b = inp()
    xk,yk = inp()
    xq,yq = inp()
    king,queen=set(),set()
    cnt = 0
    for j in range(4):
        king.add((xk+dx[j]*a,yk+dy[j]*b))
        queen.add((xq+dx[j]*a,yq+dy[j]*b))
        king.add((xk+dx[j]*b,yk+dy[j]*a))
        queen.add((xq+dx[j]*b,yq+dy[j]*a))
    for pos in king:
        if pos in queen:
            cnt += 1
    print(cnt) 


# ================== SOLUTION END ==================

if LOCAL:
    sys.stdout.flush()
#cfjudge
#python run.py