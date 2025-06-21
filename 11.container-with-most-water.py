#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: list[int]) -> int:
        res = 0
        l , r = 0 , len(height) - 1
        while l < r:
            area = (r-l) * min(height[l],height[r])
            res = max(res, area)
            if height[l] > height[r]:
                r -= 1
            else:
                l +=1
        return res
# @lc code=end

