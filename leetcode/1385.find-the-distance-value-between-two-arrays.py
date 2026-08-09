#
# @lc app=leetcode id=1385 lang=python3
#
# [1385] Find the Distance Value Between Two Arrays
#

# @lc code=start
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        res = 0
        for i in arr1:
            flag = True
            for j in arr2:
                o = abs(i-j)
                if o<=d:
                    flag = False
                    continue
            res += 1 if flag else 0
        return res
        
# @lc code=end

