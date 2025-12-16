#
# @lc app=leetcode id=463 lang=python3
#
# [463] Island Perimeter
#

# @lc code=start
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row,col = len(grid),len(grid[0])
        perimeter,visit = 0,set()
        def dfs(r,c):
            if (r,c) in visit:
                return
            nonlocal perimeter
            if r<0 or c<0 or r>=row or c >= col or grid[r][c] == 0:
                perimeter += 1
                return
            elif grid[r][c] == 1:
                visit.add((r,c))
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r-1,c)
            dfs(r,c-1)
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    dfs(r,c)
        return perimeter
# @lc code=end

