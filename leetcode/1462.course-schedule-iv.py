#
# @lc app=leetcode id=1462 lang=python3
#
# [1462] Course Schedule IV
# @lc code=start
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        for pre,crs in prerequisites:
            adj[crs].append(pre)
        mapy,res = {},[]
        def dfs(crs):
            if crs not in mapy:
                mapy[crs] = set()
                for pre in adj[crs]:
                    mapy[crs] |= dfs(pre)
                mapy[crs].add(crs)
            return mapy[crs] 
        for crs in range(numCourses):
            dfs(crs)
        for u,v in queries:
            res.append(u in mapy[v])
        return res

# @lc code=end

