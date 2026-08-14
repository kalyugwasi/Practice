#
# @lc app=leetcode id=1137 lang=python3
#
# [1137] N-th Tribonacci Number
#

# @lc code=start
class Solution:
    def tribonacci(self, n: int) -> int:
        arr = [0,1,1]
        if n ==0:
            return 0
        if n == 1:
            return 1
        if n < 3:
            return arr[n-1]
        for i in range(4,n+2):
            a = arr[i-4:i]
            arr.append(sum(a))
        return arr[-1]
# @lc code=end

