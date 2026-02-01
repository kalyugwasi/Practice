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
    x,n = inp()
    m = n%4
    if m==0:pos = 0
    elif m==1:pos = -n
    elif m==2:pos = 1
    else:pos = n + 1
    if x%2==0:
        print(x+pos)
    else:
        print(x-pos)



    '''
    for i in range(n):
        if x%2!=0:
            x += (i+1)
        else:
            x -= (i+1)
    print(x)
    '''

# ================== SOLUTION END ==================

if LOCAL:
    sys.stdout.flush()
#cfjudge
#python run.py