#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        final = 0
        size = len(s)
        for l in range(size):
            for r in range(l+1,size+1):
                if s[l:r] == s[l:r][::-1] and s[l:r] != ["",None]:
                    final += 1
        return final
        
# @lc code=end

