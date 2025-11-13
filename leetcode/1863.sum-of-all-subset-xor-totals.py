#
# @lc app=leetcode id=1863 lang=python3
#
# [1863] Sum of All Subset XOR Totals
#

# @lc code=start
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(i,total):
            if i== len(nums):
                return total
            return dfs(i+1,total ^ nums[i]) + dfs(i+1,total)
        return dfs(0,0)
# @lc code=end

