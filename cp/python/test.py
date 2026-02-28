def canConstruct():

print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(canConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e","ee","eee","eeee","eeeee","eeeeee"]))













"""
def bestsum(target,numbers):
    table = [None]*(target+1)
    table[0] = []
    for i in range(target+1):
        if table[i] is not None:
            for num in numbers:
                comb = table[i] + [num]
                if num+i <= target and (not table[num+i] or len(comb)<len(table[num+i])):
                    table[num+i] = comb
    return table[target]

print(bestsum(7,[5,3,4]))
print(bestsum(8,[2,3,5]))
print(bestsum(300,[7,14]))
print(bestsum(7,[2,3]))
print(bestsum(7,[2,4]))
print(bestsum(100,[25,1,2,3]))
print(bestsum(100,[1,2,3,25]))
print(bestsum(7,[5,3,7,4]))
"""
"""
def howsum(target,numbers):
    table = [None]*(target+1)
    table[0] = []
    for i in range(target+1):
        if table[i] is not None:
            for num in numbers:
                if num+i <= target:
                    table[num+i] = table[i] + [num]
    return table[target]

print(howsum(7,[5,3,4]))
print(howsum(8,[2,3,5]))
print(howsum(300,[7,14]))
print(howsum(7,[2,3]))
print(howsum(7,[2,4]))
print(howsum(7,[5,3,7,4]))
"""


"""
def cansum(target,numbers):
    table = [False]*(target+1)
    table[0] = True
    for i in range(target):
        if table[i]:
            for num in numbers:
                if num+i <= target: table[num+i] = True
    return table[target] 

print(cansum(7,[5,3,4,7]))
print(cansum(7,[2,3]))
print(cansum(7,[2,4]))
print(cansum(8,[2,3,5]))
print(cansum(300,[7,14]))
"""


"""def printer(m,table):
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
print(grid(30,30))
"""
