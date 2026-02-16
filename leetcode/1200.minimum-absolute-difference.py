#
# @lc app=leetcode id=1200 lang=python3
#
# [1200] Minimum Absolute Difference
#

# @lc code=start
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        a = sorted(arr)
        n = len(a)
        prev = a[0]
        m = float("inf")
        res = []
        for i in range(1,n):
            diff = abs(a[i]-prev)
            if diff < m:
                res = []
            if diff <= m:
                m = diff
                res.append([prev,a[i]])
            prev = a[i]
        return res
# @lc code=end

