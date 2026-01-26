import sys,heapq

if "input.txt" in sys.argv:
    sys.stdin = open("input.txt","r")
    sys.stdout = open("output.txt", "w")

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    # x,y,z = map(int,input().split())
    # s = list(map(int,input().split()))
    # p = list(map(str,input().strip()))
    moves = 10
    if (n-1)%3==0 or (n+1)%3==0:
        print("First")
    else:
        print("Second")