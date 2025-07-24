#
# @lc app=leetcode id=2529 lang=python3
#
# [2529] Maximum Count of Positive Integer and Negative Integer
#

# @lc code=start
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        import bisect
        neg = bisect.bisect_left(nums,0)
        pos = bisect.bisect_left(nums,1)
        return max(neg,len(nums)-pos)
        
# @lc code=end

