#
# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#

# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i : i[0])
        res = 0
        prev = intervals[0][1]
        for start,end in intervals[1:]:
            if start>=prev:
                prev = end
            else:
                res+=1
                prev = min(prev,end)
        return res
            # @lc code=end

