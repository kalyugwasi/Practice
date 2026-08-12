#
# @lc app=leetcode id=1588 lang=python3
#
# [1588] Sum of All Odd Length Subarrays
#

# @lc code=start
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res = 0
        n = len(arr)
        for i in range(n):
            for j in range(1,n-1+1,2):
                res += sum(arr[i:j+i])
        return res 
# @lc code=end

