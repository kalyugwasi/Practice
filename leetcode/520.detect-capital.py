#
# @lc app=leetcode id=520 lang=python3
#
# [520] Detect Capital
#

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if (word == word.upper()) or (word[0] == word[0].upper() and word[1:] == word[1:].lower() or word == word.lower()):
            return True
        else:
            return False
# @lc code=end

