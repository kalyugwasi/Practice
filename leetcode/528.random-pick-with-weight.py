#
# @lc app=leetcode id=528 lang=python3
#
# [528] Random Pick with Weight
#

# @lc code=start
class Solution:

    def __init__(self, w: List[int]):
        self.prefix = []
        total = 0
        for wei in w:
            total += wei
            self.prefix.append(total) 
        self.total = total

    def pickIndex(self) -> int:
        l,r = 0,len(self.prefix)        
        target = random.uniform(0,self.total)
        while l<r:
            mid = (l+r)//2
            if self.prefix[mid] < target:
                l = mid +1
            else:
                r = mid
        return l


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
# @lc code=end

