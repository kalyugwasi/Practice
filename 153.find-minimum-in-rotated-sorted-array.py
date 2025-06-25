#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l , r = 0 , len(nums) - 1
        res = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            m = (l+r) // 2
            res = min(res , nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res

# @lc code=end

