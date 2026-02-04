import sys,os,heapq
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
    hp = [[k,i+1] if a[i]%k==0 else [a[i]%k,i+1] for i in range(n)]
    hp.sort(key=lambda x:(-x[0],x[1]))
    print(*[idx for _,idx in hp])
    
    '''
    a = [[-val,0,idx+1] for idx,val in enumerate(ints())]
    res = []
    heapq.heapify(a)
    while a:
        val,_,idx = heapq.heappop(a)
        val = -val
        if val>0:
            val -= k
            if val>0:
                heapq.heappush(a,[-val,0,idx])
            else:
                res.append(idx)
    print(*res)
    ''' 
    

# ================== SOLUTION END ==================

if LOCAL:
    sys.stdout.flush()
#cfjudge
#python run.py