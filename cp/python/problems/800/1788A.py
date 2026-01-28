import sys,os,math
from collections import deque,heapq,Counter
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
strs = lambda: input().strip()

# ================== SOLUTION START ==================

t = int1()
for _ in range(t):
    n = int1()
    a = ints()
    s = Counter(a)
    if s[2]%2!=0:
        print(-1)
    else:
        i = s[2]//2
        if i==0:
            print(1)
        else:
            for p in range(n):
                if a[p] ==2:
                    i -= 1
                if i == 0:
                    print(p+1)
                    break
            
            

            


# ================== SOLUTION END ==================