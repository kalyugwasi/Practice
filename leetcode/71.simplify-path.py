#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for a in path.split("/"):
            if a not in ["",".",".."]:
                stack.append(a)
            elif a == ".." and stack:
                stack.pop()
        return "/" if not stack else "/"+"/".join(stack)

# @lc code=end

