import sys
#from collections import Counter
m = sys.stdin.readline
t = str(m())
cur,res,out = "",0,0
for s in t:
    if not cur:
        cur = s
        res = 1
    elif s == cur:
        res+=1
    elif s != cur:
        cur=s
        res=1
    out = max(out,res)
print(out)


    