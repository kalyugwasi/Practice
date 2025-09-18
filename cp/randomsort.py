import random

class Sol:
    def randomsort(self, lis: list, res: list):
        print("pass :")
        if lis == res:
            return lis
        else:
            j = random.shuffle(lis)
            while j not in mapy:
                mapy.append(j)
                return self.randomsort(lis, res)
mapy = []
lis = [2, 7, 4, 9, 3, 5, 0, 1]
res = sorted(lis)
s = Sol()
print(s.randomsort(lis, res))
