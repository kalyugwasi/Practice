import sys
m = sys.stdin.readline
n = int(m())
if n % 4 not in [0,3]:
    print("NO")
else:
    print("YES")
    a1,a2 = [],[]
    if n % 4 == 0:
        for i in range(1, n // 2 + 1):
            if i % 2 == 1:
                a1.append(i)
                a1.append(n - i + 1)
            else:
                a2.append(i)
                a2.append(n - i + 1)
    else:
        a1.extend([1, 2])
        a2.append(3)
        for i in range(4, n // 2 + 1):
            if (i - 3) % 2 == 0:
                a1.append(i)
                a1.append(n - i + 1)
            else:
                a2.append(i)
                a2.append(n - i + 1)
    print(len(a1))
    print(*a1)
    print(len(a2))
    print(*a2)

'''
import sys
m = sys.stdin.readline
t = int(m())
arr = [n for n in range(1,t+1)]
a1,a2=[],[]
target = sum(arr) // 2
if t % 4 not in (0, 3):
    print("NO")
    sys.exit()
else:
    a1_sum = 0
    print("YES")
    for i in range(t-1,-1,-1):
        if arr[i] <= target  - a1_sum:
            a1.append(arr[i])
            a1_sum+= arr[i]
    a2 = [item for item in arr if item not in a1]
    print(len(a2))
    print(*a2)
    print(len(a1))
    print(*a1)
'''