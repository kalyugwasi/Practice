#
# @lc app=leetcode id=542 lang=python3
#
# [542] 01 Matrix
#

# @lc code=start
from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n,m = len(mat),len(mat[0])
        res = [[-1]*m for _ in range(n)]
        q = deque()
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    q.append((i,j))
                    res[i][j] = 0
        while q:
            r,c = q.popleft()
            for dr,dc in [(-1,0),(0,-1),(1,0),(0,1)]:
                nr,nc = dr+r , dc+c
                if n>nr>=0 and m>nc>=0 and res[nr][nc] == -1:
                    res[nr][nc] = res[r][c] + 1
                    q.append((nr, nc))
        return res
# @lc code=end

