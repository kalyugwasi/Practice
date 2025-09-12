#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float('-inf')
        currentSum = 0
        for num in nums:
            currentSum += num
            if currentSum > maxSum:
                maxSum = currentSum
            if currentSum < 0:
                currentSum = 0
        return maxSum
# @lc code=end

