#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: list[int]) -> int:
        if not height: return 0
        l , r = 0 , len(height) - 1
        leftMax , Rightmax = height[l] , height[r]
        res = 0
        while l < r:
            if leftMax < Rightmax:
                l += 1
                leftMax = max(leftMax , height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                Rightmax =max(Rightmax , height[r])
                res += Rightmax - height[r]
        return res        
# @lc code=end

