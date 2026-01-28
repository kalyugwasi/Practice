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
if not LOCAL:
    sys.stdin = open(0, 'rb')
    input = lambda: sys.stdin.readline().decode().rstrip()
else:
    input = sys.stdin.readline
int1 = lambda: int(input())
str1 = lambda: input()
inp = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
strs = lambda: input().split()

# ================== SOLUTION START ==================

t = int1()
for _ in range(t):
    a,b,c,d = ints()
    move = -1
    if d<b or (a+(d-b))<c:
        move = -1
    else:
        move += (d-b)+abs(a+(d-b)-c)+1
    print(move)
    

# ================== SOLUTION END ==================