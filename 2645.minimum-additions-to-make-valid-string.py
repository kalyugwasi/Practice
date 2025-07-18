#
# @lc app=leetcode id=2645 lang=python3
#
# [2645] Minimum Additions to Make Valid String
#

# @lc code=start
class Solution:
    def addMinimum(self, word: str) -> int:
        it = 0
        result = 0
        while it < len(word):
            if word[it:it+3] == "abc":
                it +=3
            elif word[it:it+2] in ["ab","bc","ac"]:
                result +=1
                it += 2
            else:
                result += 2
                it += 1
        return result
        
# @lc code=end

