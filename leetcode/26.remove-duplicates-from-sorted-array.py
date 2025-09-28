#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        i = 0
        for n in range(len(nums)):
            if nums[i]!=nums[n]:
                i+=1
                nums[i]=nums[n]
        return i+1
# @lc code=end

