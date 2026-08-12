#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l = r = 1
        out = [1]*n
        for i in range(n):
            out[i] = l
            l *= nums[i]
        for i in range(n-1,-1,-1):
            out[i] *= r
            r *= nums[i]
        return out
        
# @lc code=end

