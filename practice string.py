str1 = "ABABAB"
str2 = "ABAB"
for i in range(len(str1)):
    lenstr = str1[i:]
    if lenstr // str1:
        print(lenstr)