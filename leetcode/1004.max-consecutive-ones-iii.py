#
# @lc app=leetcode id=1004 lang=python3
#
# [1004] Max Consecutive Ones III
#

# @lc code=start
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        result = 0
        left = 0
        for right in range(len(nums)):
            if nums[right]==0:
                k -= 1
            while k<0:
                if nums[left] == 0:
                    k +=1
                left += 1
            result = max(result,right-left +1)
        return result
# @lc code=end

