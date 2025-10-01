#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: list[int]) -> int:
        water = 0
        if not height:
            return water
        l,r=0,len(height)-1
        lm,rm=height[l],height[r]
        while l<r:
            if lm<rm:
                l+=1
                if height[l]<lm:
                    lm = lm
                else:
                    lm = height[l]
                water += lm - height[l]
            else:
                r-=1
                if height[r]<rm:
                    rm = rm
                else:
                    rm = height[r]
                water += rm - height[r] 
        return water
# @lc code=end

