#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
class Solution(object):
    def maxProduct(self, nums):
        a=b=r=nums[0]
        for i in range(1,len(nums)):
            n=nums[i]
            if n<0:
                a,b=b,a
            a=max(n,a*n)
            b=min(n,b*n)
            r=max(r,a)
        return r
        
# @lc code=end

