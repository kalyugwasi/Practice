#
# @lc app=leetcode id=1046 lang=python3
#
# [1046] Last Stone Weight
#

# @lc code=start
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            x,y = heapq.heappop(stones),heapq.heappop(stones)
            heapq.heappush(stones,x-y)
        stones.append(0)
        return abs(stones[0])
# @lc code=end

