from itertools import accumulate
print(list(accumulate(range(1,10))))
print(list(accumulate(range(10,1,-1)))[::-1])