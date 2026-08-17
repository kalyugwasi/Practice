#
# @lc app=leetcode id=1922 lang=python3
#
# [1922] Count Good Numbers
#

# @lc code=start
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = int(1e9)+7
        even = (n+1)//2
        odd = n//2
        return (pow(5,even,mod)*pow(4,odd,mod))%mod
        
# @lc code=end

