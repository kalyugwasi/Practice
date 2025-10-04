#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start
# O(n*k)
# #class Solution:
#    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
#        l , r = 0 , k-1
#        res = []
#        while r < len(nums):
#            res.append(max(nums[l:r+1]))
#            l += 1
#            r += 1
#        return res
from typing import List
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []
        if k==1:
            return nums
        dq,res = deque(),[]
        l=r=0
        while r < len(nums):
            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()
            dq.append(r)
            if l > dq[0]:
                dq.popleft()
            if (r+1) >= k:
                res.append(nums[dq[0]])
                l += 1
            r += 1
        return res
sol = Solution()
print(sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3))
        
# @lc code=end 