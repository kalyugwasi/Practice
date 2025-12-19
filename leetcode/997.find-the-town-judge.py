#
# @lc app=leetcode id=997 lang=python3
#
# [997] Find the Town Judge
#

# @lc code=start
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        dothey = {i+1:0 for i in range(n)}
        trustedby = {i+1:0 for i in range(n)}

        for trustie,trusted in trust:
            if dothey[trustie] == 0:
                dothey[trustie] = set()
            dothey[trustie].add(trusted)
            trustedby[trusted] += 1
        
        for person in range(1,n+1):
            if dothey[person] == 0 and trustedby[person] == n-1:
                return person
        
        return -1 
# @lc code=end

