#
# @lc app=leetcode id=344 lang=python3
#
# [344] Reverse String
#

# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        for i in range(len(s) // 2):
            s[i], s[-(i + 1)] = s[-(i + 1)], s[i]

        
# @lc code=end

