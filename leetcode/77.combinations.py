#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def dfs(i,sub):
            if len(sub) == k:
                res.append(sub.copy())
                return
            elif i > n or len(sub) > k:
                return 
            sub.append(i)
            dfs(i+1,sub)
            sub.pop()
            dfs(i+1,sub)
        dfs(1,[])
        return res
# @lc code=end

