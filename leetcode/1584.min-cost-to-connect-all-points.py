#
# @lc app=leetcode id=1584 lang=python3
#
# [1584] Min Cost to Connect All Points
#

# @lc code=start
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = {i:[] for i in range(n)}
        visit = set()
        for i in range(n):
            x1,y1 = points[i]
            for j in range(i+1,n):
                x2,y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                adj[i].append([dist,j])
                adj[j].append([dist,i])
        #prim's
        res = 0
        minH = [[0,0]]
        while len(visit) < n:
            cost, i = heapq.heappop(minH)
            if i in visit:
                continue
            res += cost
            visit.add(i)
            for neiCost,nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minH,[neiCost,nei])
        return res
        
# @lc code=end

