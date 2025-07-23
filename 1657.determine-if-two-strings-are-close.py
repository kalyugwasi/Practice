#
# @lc app=leetcode id=1657 lang=python3
#
# [1657] Determine if Two Strings Are Close
#

# @lc code=start
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        a = Counter(word1)
        b = Counter(word2)
        if (sorted(a.values()) == sorted(b.values()) and
            sorted(a.keys()) == sorted(b.keys())):
            return True
        else: return False
        
# @lc code=end

