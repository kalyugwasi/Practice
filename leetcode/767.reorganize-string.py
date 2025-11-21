#
# @lc app=leetcode id=767 lang=python3
#
# [767] Reorganize String
#

# @lc code=start
class Solution:
    def reorganizeString(self, s: str) -> str:
        a = Counter(s)
        maxHeap = [[-cnt,char] for char,cnt in a.items()]
        res,prev = "",None 
        heapq.heapify(maxHeap)
        while maxHeap or prev:
            if not maxHeap and prev:
                return ""
            cnt,char = heapq.heappop(maxHeap)
            res += char
            cnt += 1
            if prev:
                heapq.heappush(maxHeap,prev)
                prev = None
            if cnt != 0:
                prev = [cnt,char]
        return res
# @lc code=end

