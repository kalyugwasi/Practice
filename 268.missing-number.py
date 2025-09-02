#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        mx = len(nums)
        for i in range(mx+1):
            if i not in nums:
                return i        
        """
        return (sum(range(len(nums)+1))-sum(nums))
        
# @lc code=end

