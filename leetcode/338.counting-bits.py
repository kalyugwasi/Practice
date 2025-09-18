#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#

# @lc code=start
class Solution:
    def countBits(self, n: int) -> List[int]:
        out = [0]
        def count(n:int):
            res = 0
            while n:
                if n&1:
                    res+=1
                n>>=1
            return res
        for i in range(1,n+1):
            out.append(count(i))
        return out
# @lc code=end

