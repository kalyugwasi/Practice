#
# @lc app=leetcode id=2073 lang=python3
#
# [2073] Time Needed to Buy Tickets
#

# @lc code=start
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        for i in range(len(tickets)):
            if i <= k:
                time += min(tickets[i], tickets[k])
            else:
                time += min(tickets[i], tickets[k] - 1)
        return time
        
# @lc code=end

