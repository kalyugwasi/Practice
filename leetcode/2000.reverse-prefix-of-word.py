#
# @lc app=leetcode id=2000 lang=python3
#
# [2000] Reverse Prefix of Word
#

# @lc code=start
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        found = False
        for k,v in enumerate(word):
            if v == ch:
                found = True
                break
        return word[:k+1][::-1] +word[k+1:] if found == True else word
# @lc code=end

