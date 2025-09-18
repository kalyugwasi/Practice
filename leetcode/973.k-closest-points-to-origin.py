#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#

# @lc code=start
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x,y in points:
            dist = sqrt((x**2) + (y**2))
            minHeap.append([dist,x,y])
        res = []
        heapq.heapify(minHeap)
        while k>0:
            dist , x, y  = heapq.heappop(minHeap)
            res.append([x,y])
            k -= 1
        return res
        
# @lc code=end

