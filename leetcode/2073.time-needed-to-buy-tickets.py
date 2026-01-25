#
# @lc app=leetcode id=2073 lang=python3
#
# [2073] Time Needed to Buy Tickets
#

# @lc code=start
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        queue = deque(range(len(tickets)))
        while queue:
            time += 1
            q = queue.popleft()
            tickets[q] -= 1
            if tickets[q] == 0 and k == q:
                return time
            if tickets[q] >0:
                queue.append(q)
        return time
# @lc code=end

