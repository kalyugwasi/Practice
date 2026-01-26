import sys,heapq

if "input.txt" in sys.argv:
    sys.stdin = open("input.txt","r")
    sys.stdout = open("output.txt", "w")

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    # x,y,z = map(int,input().split())
    # p = list(map(str,input().strip()))
    