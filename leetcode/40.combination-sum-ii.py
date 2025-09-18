#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if total > target:
                return
            prev = -1
            for j in range(i, len(candidates)):
                if candidates[j] == prev:
                    continue
                cur.append(candidates[j])
                dfs(j + 1, cur, total + candidates[j])
                cur.pop()
                prev = candidates[j]
        dfs(0, [], 0)
        return res

        
# @lc code=end

