#
# @lc app=leetcode id=1342 lang=python3
#
# [1342] Number of Steps to Reduce a Number to Zero
#

class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        while num !=0:
            count +=1
            a= num%2
            if a ==0:
                num/=2
            else:
                num-=1
        return count
        
# @lc code=end

