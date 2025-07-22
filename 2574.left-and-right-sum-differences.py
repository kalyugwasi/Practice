#
# @lc app=leetcode id=2574 lang=python3
#
# [2574] Left and Right Sum Differences
#

# @lc code=start
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        result = []
        left = 0
        for num in nums:
            right = total-left-num
            result.append(abs(left-right))
            left += num
        return result
        
# @lc code=end

