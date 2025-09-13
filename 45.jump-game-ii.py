#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        dp = [n+1]*n
        dp[0] = 0
        for i in range(n):
            for j in range(i+1,min(i+nums[i]+1,len(nums))):
                dp[j] = min(dp[i]+1,dp[j])
        return dp[-1]

        
# @lc code=end

