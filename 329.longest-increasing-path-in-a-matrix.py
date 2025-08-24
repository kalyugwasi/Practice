#
# @lc app=leetcode id=329 lang=python3
#
# [329] Longest Increasing Path in a Matrix
#

# @lc code=start
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        row,col = len(matrix),len(matrix[0])
        dp = {}
        def dfs(r,c,prev):
            if r<0 or r==row or c<0 or c==col or matrix[r][c] <= prev:
                return 0
            if (r,c) in dp:
                return dp[(r,c)]
            res = 1
            res = (max(res,dfs(r+1,c,matrix[r][c]) + 1,
                    dfs(r,c-1,matrix[r][c]) + 1,
                    dfs(r-1,c,matrix[r][c]) + 1,
                    dfs(r,c+1,matrix[r][c]) + 1))
            dp[(r,c)] = res
            return res 
        for r in range(row):
            for c in range(col):
                dfs(r,c,-1)
        return max(dp.values())
                
# @lc code=end

