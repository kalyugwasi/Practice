import sys,os
import itertools
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
    n = int1()
    a = ints()
    if a == [0]*n:
        print(0)
    else:
        count = 0
        igrp = False
        for x in a:
            if x != 0 and not igrp:
                count += 1
                igrp = True
            elif x == 0:
                igrp = False
        if count == 1:
            print(1)
        else:
            print(2)
    

# ================== SOLUTION END ==================

if LOCAL:
    sys.stdout.flush()
#cfjudge
#python run.py