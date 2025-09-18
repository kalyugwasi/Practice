#
# @lc app=leetcode id=2352 lang=python3
#
# [2352] Equal Row and Column Pairs
#

# @lc code=start
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        trans = Counter(zip(*grid))
        grid = Counter(map(tuple,grid))
        return sum(trans[t]*grid[t] for t in trans)

        
# @lc code=end

