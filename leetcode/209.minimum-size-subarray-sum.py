#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float("inf")
        summ = l = 0
        for r in range(len(nums)):
            summ += nums[r]
            while summ >= target:
                res = min(res,r-l+1)
                summ -= nums[l]
                l += 1 
        return res if res != float("inf") else 0
# @lc code=end

