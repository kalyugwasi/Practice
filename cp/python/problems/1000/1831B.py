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
def cnt(a):
    n = len(a)
    counts = {}
    i = 0
    while i <n:
        val = a[i]
        cnt = 1
        while i+cnt<n and a[i+cnt]==val:
            cnt += 1
        counts[val] = max(counts.get(val,0),cnt)
        i += cnt
    return counts
t = int1()
for _ in range(t):
    n = int1()
    a,b = ints(),ints()
    cnta,cntb = cnt(a),cnt(b)
    num = set(cnta.keys()) | set(cntb.keys())
    mx = 0
    for i in num:
        total = cnta.get(i,0) + cntb.get(i,0)
        mx = max(mx,total)
    print(mx)

    
    

# ================== SOLUTION END ==================

if LOCAL:
    sys.stdout.flush()
#cfjudge
#python run.py