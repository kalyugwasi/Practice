#
# @lc app=leetcode id=912 lang=python3
#
# [912] Sort an Array
#

# @lc code=start
class Solution:
    
    def mergesort(self,unsorted:List[int]):
        n = len(unsorted)
        if n == 1:
            return unsorted
        mid = n//2
        left = unsorted[mid:]
        right = unsorted[:mid]
        sortedleft,sortedright = self.mergesort(left),self.mergesort(right)
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


    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergesort(nums)
    
        
# @lc code=end

