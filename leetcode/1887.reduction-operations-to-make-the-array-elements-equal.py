#
# @lc app=leetcode id=1887 lang=python3
#
# [1887] Reduction Operations to Make the Array Elements Equal
#

# @lc code=start
class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        cnt = 0
        for i in range(n-2,-1,-1):
            if nums[i] < nums[i+1]:
                cnt += n-i-1
        return cnt

# @lc code=end

