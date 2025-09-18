#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#

# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow , fast = 0, 0 
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = 0
        while (slow!=fast):
            slow = nums[slow]
            fast = nums[fast]
        return slow
        
# @lc code=end

