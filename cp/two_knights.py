import sys
for i in range(1,int(sys.stdin.readline())+1):
    print(int((i**2)*(((i**2)-1)/2)-(4*(i-1)*(i-2))))