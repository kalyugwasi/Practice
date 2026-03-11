#
# @lc app=leetcode id=1391 lang=python3
#
# [1391] Check if There is a Valid Path in a Grid
#

# @lc code=start
class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        n,m = len(grid),len(grid[0])
        directions = {
        1: [(0, -1), (0, 1)],  # Street 1: Horizontal (left, right)
        2: [(1, 0), (-1, 0)],  # Street 2: Vertical (down, up)
        3: [(0, -1), (1, 0)],  # Street 3: Left-Down (left, down)
        4: [(0, 1), (1, 0)],   # Street 4: Right-Down (right, down)
        5: [(0, -1), (-1, 0)], # Street 5: Left-Up (left, up)
        6: [(0, 1), (-1, 0)]   # Street 6: Right-Up (right, up)
        }
        visited = set()
        def dfs(i,j):
            if (i,j) in visited:
                return False
            if i==n-1 and j==m-1:
                return True
            visited.add((i,j))
            for dx,dy in directions[grid[i][j]]:
                ni,nj = i+dx, j+dy
                if 0<=ni < n and 0 <= nj<m:
                    if (-dx,-dy) in directions[grid[ni][nj]]:
                        if dfs(ni,nj):
                            return True
            return False
        return dfs(0,0)
        
# @lc code=end

