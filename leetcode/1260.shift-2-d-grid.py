#
# @lc app=leetcode id=1260 lang=python3
#
# [1260] Shift 2D Grid
#

# @lc code=start
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        r,c = len(grid),len(grid[0])
        grid = deque([j for i in grid for j in i])
        grid.rotate(k)
        grid = list(grid)
        return [grid[i:i+c] for i in range(0,len(grid),c)]
# @lc code=end

