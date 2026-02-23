#
# @lc app=leetcode id=1992 lang=python3
#
# [1992] Find All Groups of Farmland
#

# @lc code=start
class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        row,col = len(land),len(land[0])
        visit = set()
        res = []
        def dfs(r,c):
            if r<0 or c<0 or r>=row or c>=col or land[r][c] == 0 or (r,c) in visit:
                return 
            visit.add((r,c))
            self.ma,self.mb = max(self.ma,r),max(self.mb,c)
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r-1,c)
            dfs(r,c-1)
        for r in range(row):
            for c in range(col):
                if land[r][c] == 1 and (r,c) not in visit:
                    self.ma,self.mb = r,c
                    dfs(r,c)
                    res.append([r,c,self.ma,self.mb])
        return res
# @lc code=end

