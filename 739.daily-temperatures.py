#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            for j in range(i+1 ,len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    res[i] = (j-i)
                    break
        return res

# @lc code=end

