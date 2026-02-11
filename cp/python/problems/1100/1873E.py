import sys,os
def setup_io():
    try:
        base = os.path.dirname(os.path.abspath(__file__))
        judge = os.path.join(base,"..","judge")
        inpth = os.path.join(judge,"input.txt")
        outpth = os.path.join(judge,"output.txt")
        if os.path.exists(inpth):
            sys.stdin = open(inpth,"r")
            sys.stdout = open(outpth,"w")
            return True
    except:
        pass
    return False
LOCAL = setup_io()
input = sys.stdin.readline
int1 = lambda: int(input())
str1 = lambda: input().strip()
ints1 = lambda: list(map(int,str1()))
def inp(): return map(int, input().split())
def ints(): return list(map(int, input().split()))
def strs(): return list(map(str,str1()))
def mint(): return map(int, input().split())
def grid(n): return [ints() for _ in range(n)]
def sgrid(n): return [input() for _ in range(n)]

# ================= SOLUTION START =================
def check(mid, heights, x):
	units = 0
	n = len(heights)  
	for i in range(n):  
		if heights[i] < mid:
			units += (mid - heights[i])
	return units <= x
t = int1()
for _ in range(t):
    n,x = inp()
    a = ints()
    si, ei, ans = 1, int(1e12), -1
    while si <= ei:
        mid = si + (ei - si) // 2
        if check(mid, a, x):
            ans = mid   
            si = mid + 1  
        else:
            ei = mid - 1
    print(ans)
        

# ================== SOLUTION END ==================

if LOCAL:
    sys.stdout.flush()
