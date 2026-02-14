#
# @lc app=leetcode id=1664 lang=python3
#
# [1664] Ways to Make a Fair Array
#

# @lc code=start
class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = 0
        odd,even = [0]*(n+1),[0]*(n+1)
        for i,num in enumerate(nums):
            if i%2:
                odd[i+1],even[i+1] = odd[i] + num,even[i]
            else:
                odd[i+1],even[i+1] = odd[i],even[i] + num
        for i in range(1,n+1):
            odd1,even1 = odd[i-1],even[i-1]
            odd2,even2 = even[-1]-even[i],odd[-1]-odd[i]
            if odd1+odd2==even1+even2:
                cnt += 1
        return cnt
# @lc code=end

