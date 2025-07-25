#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#

# @lc code=start
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        visit = set()
        q = deque()

        def addRoom(r,c):
            if (r<0 or r>=rows or c<0 or c>=cols or (r,c) in visit or grid[r][c] == 0):
                return
            visit.add((r,c))
            q.append([r,c])   
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    q.append([r,c])
                    visit.add((r,c))
        dist= 3
        res = 0
        while q:
            for i in range(len(q)):
                r,c=q.popleft()
                grid[r][c] = dist
                addRoom(r+1,c)
                addRoom(r-1,c)
                addRoom(r,c+1)
                addRoom(r,c-1)
            dist += 1
            res = max(grid[r][c],res)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        return res-3 if res > 3 else 0
        
# @lc code=end

