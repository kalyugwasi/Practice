#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def backtracking(i,subset):
            if i == len(nums):
                res.append(subset[::])
                return
            subset.append(nums[i])
            backtracking(i+1,subset)
            subset.pop()

            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtracking(i+1,subset)
        backtracking(0,[])
        return res
        
# @lc code=end

