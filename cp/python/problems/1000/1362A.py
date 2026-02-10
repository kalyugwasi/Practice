import sys,os,math
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
int1 = lambda: int(input()) #for reading a single number
str1 = lambda: input().strip() #for spliting a char in parts
ints1 = lambda: list(map(int,str1())) #mostly for 0,1
def inp(): return map(int, input().split()) #mainly for multiple known variables
def ints(): return list(map(int, input().split())) #for numerical lists
def strs(): return list(map(str,str1())) #for string list

# ================= SOLUTION START =================

t = int1()
for _ in range(t):
    a,b = inp()
    ra,rb = a,b
    while ra%2==0:
        ra//=2
    while rb%2==0:
        rb//=2
    if ra!=rb:
        print(-1)
    else:
        a//=ra
        b//=rb
        a = int(math.log2(a))
        b = int(math.log2(b))
        res = math.ceil(abs(a-b)/3)
        print(res)
        
    

# ================== SOLUTION END ==================

if LOCAL:
    sys.stdout.flush()
#cfjudge
#python run.py