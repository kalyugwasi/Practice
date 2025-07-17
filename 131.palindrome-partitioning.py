#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        part =[]
        def dfs(i):
            if i>= len(s):
                res.append(part.copy())
                return
            for j in range(i,len(s)):
                if self.isPali(s,i,j):
                    part.append(s[i:j+1])
                    dfs(j+1 )
                    part.pop()
        dfs(0)
        return res
    def isPali(self,s,l,r):
        while l<r:
            if s[l] != s[r]:
                return False
            l,r = l+1,r-1
        return True

# @lc code=end

