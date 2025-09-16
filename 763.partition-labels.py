#
# @lc app=leetcode id=763 lang=python3
#
# [763] Partition Labels
#

# @lc code=start
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        for i,v in enumerate(s):
            last[v] = i
        size=end=0
        res = []
        for i,v in enumerate(s):
            size+=1
            end = max(end,last[v])
            if i ==end:
                res.append(size)
                size=0
        return res
        
# @lc code=end

