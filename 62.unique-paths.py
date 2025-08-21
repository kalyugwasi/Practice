#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0] * n for _ in range(m)]
        for r in range(m):
            for c in range(n):
                if r == 0 or c == 0:
                    grid[r][c] = 1
                else:
                    grid[r][c] = grid[r-1][c]+grid[r][c-1]
        return grid[r][c] 

        
# @lc code=end

