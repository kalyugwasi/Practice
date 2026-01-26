import sys,heapq

if "input.txt" in sys.argv:
    sys.stdin = open("input.txt","r")
    sys.stdout = open("output.txt", "w")

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(str,input().strip()))
    s =  ["#"] + s + ["#"]
    count,step = 0,0
    for i in range(len(s)):
        if s[i] == ".":
            step += 1
            if step == 3:
                count = 2
                break
        else:
            count += step
            step = 0
    print(count)
