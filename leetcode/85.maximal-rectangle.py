#
# @lc app=leetcode id=85 lang=python3
#
# [85] Maximal Rectangle
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights.append(0)
        res = 0
        for i,h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                res = max(res,height*width)
            stack.append(i)
        return res 
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n,m = len(matrix),len(matrix[0])
        res = float("-inf")
        heights = [0]*n
        for col in range(m):
            for row in range(n):
                if matrix[row][col] == "1":
                    heights[row] += 1
                else:
                    heights[row] = 0
            res = max(res, self.largestRectangleArea(heights[:]))
        return res
        
# @lc code=end

