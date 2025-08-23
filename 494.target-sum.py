#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#

# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def bt(i,res):
            if i==len(nums):
                return 1 if res == target else 0
            if (i,res) in dp:
                return dp[(i,res)]
            dp[(i,res)] = bt(i+1,res+nums[i]) + bt(i+1,res-nums[i])
            return dp[(i,res)]
        return bt(0,0 )
        
# @lc code=end

