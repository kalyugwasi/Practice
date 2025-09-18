#
# @lc app=leetcode id=485 lang=python3
#
# [485] Max Consecutive Ones
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count ,result,right = 0,0,0
        while right < len(nums): 
            if nums[right] == 1:
                count += 1
                result = max(result,count)
            else:
                count = 0
            right += 1
        return result

           
# @lc code=end

