class Merger:
    def mergesort(self,unsorted:list):
        if len(unsorted) == 1:
            return unsorted
        mid = len(unsorted)//2
        lefty = unsorted[mid:]
        righty = unsorted[:mid]
        sortedleft,sortedright = self.mergesort(lefty),self.mergesort(righty)
        return self.merge(sortedleft,sortedright)
    def merge(self,l:list,r:list):
        res = []
        i=j=0
        while i<len(l) and j<len(r):
            if l[i]<r[j]:
                res.append(l[i])
                i+=1
            else:
                res.append(r[j])
                j+=1
        res.extend(l[i:])
        res.extend(r[j:])
        return res


inp = [8,2,7,3,9,1,0,4,6,5]
p = Merger()
print(p.mergesort(inp))