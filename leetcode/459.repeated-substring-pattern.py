#
# @lc app=leetcode id=459 lang=python3
#
# [459] Repeated Substring Pattern
#

# @lc code=start
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        if n <2:
            return False
        res=""
        for i in range(n//2):
            res += s[i]
            if n%len(res) == 0:
                    if res * (n//len(res))==s:
                        return True
        return False

# @lc code=end

