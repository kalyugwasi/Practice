#
# @lc app=leetcode id=678 lang=python3
#
# [678] Valid Parenthesis String
#

# @lc code=start
class Solution:
    def checkValidString(self, s: str) -> bool:
        l=h=0
        for c in s:
            if c == "(":
                l+=1
                h+=1
            elif c == ")":
                l-=1
                h-=1
            else:
                l-=1
                h+=1
            if h < 0:return False
            if l < 0:l = 0
        return l==0
        
# @lc code=end

