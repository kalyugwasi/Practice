#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return list(set([i+1 for i in range(len(nums))]) - set(nums))
# @lc code=end

