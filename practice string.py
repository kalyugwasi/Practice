str1 = "ABABAB"
str2 = "ABAB"
nums = [2,1,5,0,4,6]
iop = "".join(map(str ,nums)) 
paren = {')':'(','}':'{',']':'['}
empty= []
def stacky()
for i in str1:
    if i in empty:
        if empty and empty[-1] == paren:
            stack.pop()
        else: return False
    else: 
        empty.append(i)
    return True if not stack else False 
