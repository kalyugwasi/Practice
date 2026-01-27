#
# @lc app=leetcode id=1354 lang=python3
#
# [1354] Construct Target Array With Multiple Sums
#

# @lc code=start
class Solution:
    def isPossible(self, target: List[int]) -> bool:
        target = [-x for x in target]
        heapq.heapify(target)
        total = -sum(target)
        while True:
            largest = -heapq.heappop(target)
            rest = total - largest
            if largest == 1 or rest == 1:
                return True
            if rest == 0 or rest >= largest:
                return False
            prev = largest % rest
            if prev == 0:
                prev = rest
            heapq.heappush(target, -prev)
            total = rest + prev
# @lc code=end

