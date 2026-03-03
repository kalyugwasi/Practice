#
# @lc app=leetcode id=2698 lang=python3
#
# [2698] Find the Punishment Number of an Integer
#

# @lc code=start
class Solution:
    def punishmentNumber(self, n: int) -> int:
        res = 0
        def bt(i,cur,target,st):
            if i == len(st) or cur == target:
                return True
            for j in range(i,len(st)):
                pre = st[i:j+1]
                if bt(j+1,cur+pre,target,st):
                    return True
            return False
        def dfs(i):
            sq = i*i
            if bt(0,0,i,str(sq)):
                return sq
            return 0
        for i in range(1,n+1):
            res += dfs(i)
        return res
# @lc code=end

