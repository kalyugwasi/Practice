#
# @lc app=leetcode id=724 lang=python3
#
# [724] Find Pivot Index
#

# @lc code=start
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l,r = 0, sum(nums)
        for i,e in enumerate(nums):
            r-=e
            if l == r: return i
            l+=e
        return -1      
# @lc code=end

