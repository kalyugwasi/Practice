#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i : i[0] )
        res = [intervals[0]]
        for start,end in intervals[1:]:
            last = res[-1][1]
            if start <= last:
                res[-1][1] = max(last,end)
            else:
                res.append([start,end])
        return res
# @lc code=end

