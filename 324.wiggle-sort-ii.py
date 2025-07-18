#
# @lc app=leetcode id=324 lang=python3
#
# [324] Wiggle Sort II
#

# @lc code=start
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        n = len(nums)
        nums.sort()
        mid = (n - 1) // 2
        nums[::2], nums[1::2] = nums[mid::-1], nums[:mid:-1]
        
# @lc code=end

