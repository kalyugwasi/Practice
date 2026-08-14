#
# @lc app=leetcode id=37 lang=python3
#
# [37] Sudoku Solver
#

# @lc code=start
from collections import defaultdict
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = defaultdict(set)
        col = defaultdict(set)
        squ = defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".": continue
                row[r].add(board[r][c])
                col[c].add(board[r][c])
                squ[(r//3,c//3)].add(board[r][c])
        ref = set(str(i) for i in range(1,10))
        def possible(r,c):
                return ref - (row[r] | col[c] | squ[(r//3,c//3)])
        def dfs(l):
            if l==avail: return True
            r,c,_ = cell[l]
            li = possible(r,c)
            if not li: return False
            for i in li:
                board[r][c] = i
                row[r].add(i)
                col[c].add(i)
                squ[(r//3,c//3)].add(i)
                if dfs(l+1): return True
                board[r][c] = "."
                row[r].remove(i)
                col[c].remove(i)
                squ[(r//3,c//3)].remove(i)
            return False
        cell = []
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    ans = possible(r,c)
                    u = len(ans)
                    if u == 1:
                        board[r][c] = ans.pop()
                        continue
                    cell.append((r,c,u))
        cell.sort(key=lambda x: x[2]) 
        avail = len(cell)
        dfs(0)
        
# @lc code=end

