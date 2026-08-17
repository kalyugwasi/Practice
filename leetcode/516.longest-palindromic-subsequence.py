#
# @lc app=leetcode id=516 lang=python3
#
# [516] Longest Palindromic Subsequence
#

# @lc code=start
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        grid = [[0 if j!=i else 1 for j in range(n)] for i in range(n)]
        for r in range(n-1,-1,-1):
            for c in range(n):
                if c>r: 
                    if s[r] == s[c]:
                        grid[r][c] += grid[r+1][c-1]+2
                    else:
                        grid[r][c] += max(grid[r+1][c],grid[r][c-1])
        return grid[0][n-1]
# @lc code=end

