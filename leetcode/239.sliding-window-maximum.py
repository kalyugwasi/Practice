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
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []
        if k > len(nums):
            return [max(nums)]
        
        dq = deque()
        res = []
        for i in range(len(nums)):
            if dq and dq[0] <= i - k:
                dq.popleft()
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)
            if i >= k - 1:
                res.append(nums[dq[0]])

        return res



        
# @lc code=end 