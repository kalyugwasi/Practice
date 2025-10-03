#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        small = bigg = prices[0]
        deals =[0]
        for v in prices:
            if v<small:
                small = v
                bigg = 0
            elif v > bigg:
                bigg = v
                deals.append(v-small)
        return max(deals)
# @lc code=end

