#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []
        max_area = 0
        heights.append(0)
        i = 0
        while i < len(heights):
            if not stack or heights[i] >= heights[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                h = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, h * width)
        heights.pop()
        return max_area
sol = Solution()
print(sol.largestRectangleArea([2,1,5,6,2,3]))
print(sol.largestRectangleArea([2,4]))
print(sol.largestRectangleArea([7,1,7,2,2,4]))

# @lc code=end

