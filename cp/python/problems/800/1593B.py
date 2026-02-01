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
    n = strs()
    possible_values = ["00", "25", "50", "75"]
    res = float('inf')
    for possible_value in possible_values:
        p = n.copy()
        operations = 0
        checker_index = len(possible_value) - 1
        for i in range(len(p) - 1, -1, -1):
            if checker_index >= 0 and p[i] == possible_value[checker_index]:
                checker_index -= 1
                if checker_index < 0:
                    break
            else:
                operations += 1
        if checker_index < 0:
            res = min(res, operations)
    print(res)
    

# ================== SOLUTION END ==================

if LOCAL:
    sys.stdout.flush()
#cfjudge
#python run.py