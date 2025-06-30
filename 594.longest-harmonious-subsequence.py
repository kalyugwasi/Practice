#
# @lc app=leetcode id=594 lang=python3
#
# [594] Longest Harmonious Subsequence
#

# @lc code=start
from collections import Counter
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        a = Counter(nums)
        res = 0
        for key,values in a.items():
            if key-1 in a:
                res = max(res, a[key] + a[key-1])
            elif key+1 in a:
                res = max(res, a[key] + a[key+1])
        return res
# @lc code=end

