#
# @lc app=leetcode id=684 lang=python3
#
# [684] Redundant Connection
#

# @lc code=start
class UnionFind:
    def __init__(self, n):
        self.par, self.rank = defaultdict(int), defaultdict(int)
        for i in range(n):
            self.par[i] = i
            self.rank[i] = 0

    def find(self, n1):
        p = self.par[n1]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p2] > self.rank[p1]:
            self.par[p1] = p2
        else:
            self.par[p1] = p2
            self.rank[p2] += 1
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        unionfind = UnionFind(n)
        for u, v in edges:
            if not unionfind.union(u, v):
                return [u, v]
        
        
# @lc code=end

