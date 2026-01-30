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
    n,q = inp()
    a = ints()
    olds = sum(a)
    prefix = [0] * (n+1)
    for i in range(1,n+1):
        prefix[i] = prefix[i-1] + a[i-1]
    for __ in range(q):
        l,r,k = inp()
        sumr = prefix[r] - prefix[l-1]
        suma = (r-l+1) * k
        total = olds - sumr + suma
        print("YES" if total%2!=0 else "NO")        

# ================== SOLUTION END ==================

if LOCAL:
    sys.stdout.flush()
#cfjudge
#python run.py