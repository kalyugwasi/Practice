import sys
import bisect 
from math import comb
inp = int(sys.stdin.readline())
for _ in range(inp):
    a = list(map(int , input().split()))
    
    maxVal = a[-1]
    if a[0] == maxVal:
        print(comb(a, 3))
        continue
    
    n = int(input())
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            sumno = a[i] + a[j]
            k = bisect.bisect_right(a , maxVal - sumno ,j + 1 )
            count += n - k
        print(count)

