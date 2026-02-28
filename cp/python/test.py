def printer(m,table):
    for i in range(m):
        print(*table[i],sep="   ")
def grid(m,n):
    table = [[0 for _ in range(n+1)] for _ in range(m+1)]
    table[1][1] = 1
    for i in range(m+1):
        for j in range(n+1):
            cur = table[i][j]
            if j+1<=n:table[i][j+1] += cur
            if i+1<=m:table[i+1][j] += cur
    return printer(m,table)
    
print(grid(1,1))
print(grid(3,3))
print(grid(6,6))
print(grid(18,18))
print(grid(20,20))
