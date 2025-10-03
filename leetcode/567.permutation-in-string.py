#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m , n = len(s1), len(s2)
        s1_sorted = sorted(s1)
        for i in range(n - m + 1):
            if sorted(s2[i:i+m]) == s1_sorted:
                return True
        return False

# @lc code=end

