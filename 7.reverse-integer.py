#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

class Solution:
    def reverse(self, x: int) -> int:
        lim = 2**31
        Min,Max,res = -lim,lim-1,0
        while x:
            digit = int(math.fmod(x,10))
            x = int(x/10)
            if ((res>Max//10 or (res==Max//10 and digit>=Max%10)) or 
                (res<Min//10 or (res==Min//10 and digit<=Min%10))):
                return 0
            res = (res*10)+digit
        return res
# @lc code=end

