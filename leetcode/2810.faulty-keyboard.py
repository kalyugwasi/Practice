#
# @lc app=leetcode id=2810 lang=python3
#
# [2810] Faulty Keyboard
#

# @lc code=start
class Solution:
    def finalString(self, s: str) -> str:
        res ,listy = [], list(s)
        for char in s:
            if char == "i": res.reverse()
            else: res.append(char)
        return "".join(res)
        
        
# @lc code=end

