#
# @lc app=leetcode id=2267 lang=python3
#
# [2267]  Check if There Is a Valid Parentheses String Path
#

# @lc code=start
#from functools import cache
class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        n,m = len(grid),len(grid[0])
        if grid[0][0] == ')' or grid[n-1][m-1] == '(' or (n+m-1)%2:
            return False
        @cache
        def dfs(i,j,s):
            if i<0 or j<0:
                return False
            if grid[i][j] == ")":
                s += 1
            else:
                s -= 1
            if s<0:
                return False
            if i==0 and j ==0:
                return s==0
            return dfs(i,j-1,s) or dfs(i-1,j,s)
        return dfs(n-1,m-1,0)
@lc code=end

