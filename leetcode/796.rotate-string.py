#
# @lc app=leetcode id=796 lang=python3
#
# [796] Rotate String
#

# @lc code=start
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for ch in s:
            if goal == s:
                return True
            s = s[1:]+ch
        return False
# @lc code=end

