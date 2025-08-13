#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        out = ""
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                if s[i:j] == s[i:j][::-1] and len(s[i:j]) > len(out):
                    out = s[i:j]
        return out

        
# @lc code=end

