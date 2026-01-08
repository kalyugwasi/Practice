#
# @lc app=leetcode id=547 lang=python3
#
# [547] Number of Provinces
#

# @lc code=start
class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x):
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x

    def union(self, x1, x2):
        p1, p2 = self.find(x1), self.find(x2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n,root = len(isConnected),set()
        uf = UnionFind(n)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    uf.union(i,j)
        for i in range(n):
            root.add(uf.find(i))
        return len(root)
        
# @lc code=end

