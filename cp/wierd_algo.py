import sys
n = int(sys.stdin.readline())
res = [n]
while n != 1:
    if n%2==0:
        n//=2
    else:
        n*=3
        n+=1
    res.append(n)
print(*res)