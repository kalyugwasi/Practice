str1 = "ABABAB"
str2 = "ABAB"

for i in range(len(str1)):
    candidate = str1[i:]                      
    if len(str1) % len(candidate) == 0:       
        if candidate * (len(str1) // len(candidate)) == str1:
            print(candidate)
