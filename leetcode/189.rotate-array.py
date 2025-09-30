#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
                nums[:] = nums[n-k:] +  nums[:n-k] // fails when k is above n
        """
        n = len(nums)
        bp = (n - k) % n
        nums[:] = nums[bp:]+nums[:bp]
# @lc code=end

