import sys,os,math
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
    n = int1()

    aa,ab = 1,n-1
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            aa = n//i
            ab = n-aa
            break
    print(aa,ab)            
    
    
    '''
    res = []
    for i in range(n//2):
        res.append([math.lcm(i+1,n-i-1),i+1,n-i-1])
    res.sort()
    _,a,b = res[0]
    print(a,b)
    '''

# ================== SOLUTION END ==================

if LOCAL:
    sys.stdout.flush()
#cfjudge
#python run.py