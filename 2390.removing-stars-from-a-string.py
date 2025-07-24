#
# @lc app=leetcode id=2390 lang=python3
#
# [2390] Removing Stars From a String
#

# @lc code=start
class Solution:
    def removeStars(self, s: str) -> str:
        res = []
        for char in s:
            if char == "*":
                res.pop()
            else: res.append(char)
        return "".join(res)
        
# @lc code=end

