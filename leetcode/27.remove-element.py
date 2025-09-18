#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        for n in range(len(nums)):
            if nums[n] != val:
                nums[k] = nums[n]
                k+=1
        return k
# @lc code=end

