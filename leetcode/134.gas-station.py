#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#

# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        diff = [gas[i] - cost[i] for i in range(len(gas))]
        total=start=0
        for i in range(len(gas)):
            total += (gas[i]-cost[i])
            if total<0:
                total=0
                start=i+1
        return start

# @lc code=end

