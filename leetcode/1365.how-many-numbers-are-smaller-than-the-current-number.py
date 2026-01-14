#
# @lc app=leetcode id=1365 lang=python3
#
# [1365] How Many Numbers Are Smaller Than the Current Number
#

# @lc code=start
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        new = sorted(nums)
        res = {}
        for i,n in enumerate(new):
            if n not in res:
                res[n] = i
        return [res[n] for n in nums]
# @lc code=end

