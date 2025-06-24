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
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        output = []
        q = collections.deque()
        l = r = 0
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()    
            q.append(r)

            if l > q[0]:
                q.popleft()
            if (r+1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1
        return output


        
# @lc code=end 