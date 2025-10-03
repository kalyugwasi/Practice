#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res=l=0
        for r in s:
            count[r] = 1 + count.get(s[r],0)
            
# @lc code=end

