class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 0:
            return True
        visit = set()
        adj = {i:[] for i in range(n)}
        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        def dfs(i,prev):
            if i in visit:
                return False
            visit.add(i)
            for j in adj[i]:
                if j == prev:
                    continue
                if dfs(j,i) == False:
                    return False
            return True
        return dfs(0,-1) and len(visit) == n