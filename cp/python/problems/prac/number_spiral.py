import sys
m = sys.stdin.readline
t = int(m())
for _ in range(t):
    y,x = map(int, m().split())
    if y>x:
        ans = (y-1)*(y-1)
        if y%2!=0:
            add = x
        else:
            add = 2*y-x
        print(ans+add)
    else:
        ans = (x-1)*(x-1)
        if x%2==0:
            add = y
        else:
            add = 2*x-y
        print(ans+add)


    