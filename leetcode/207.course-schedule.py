#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mapy = {i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:
            mapy[crs].append(pre)
        visitSet = set()
        def dfs(crs):
            if crs in visitSet:
                return False
            if mapy[crs] == []:
                return True
            visitSet.add(crs)
            for pre in mapy[crs]:
                if not dfs(pre): return False
            visitSet.remove(crs)
            mapy[crs] = []
            return True
        for crs in range(numCourses):
            if not dfs(crs) : return False
        return True
        
# @lc code=end

