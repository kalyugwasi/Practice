#
# @lc app=leetcode id=846 lang=python3
#
# [846] Hand of Straights
#

# @lc code=start
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = {}
        n = len(hand)
        if n%groupSize!=0:
            return False
        for i in hand:
            count[i] = 1 + count.get(i,0)
        minH = list(count.keys())
        heapq.heapify(minH)
        while minH:
            first = minH[0]
            for i in range(first,first+groupSize):
                if i not in count:
                    return False
                count[i]-=1
                if count[i]==0:
                    if i!=minH[0]:
                        return False
                    heapq.heappop(minH)
        return True
# @lc code=end

