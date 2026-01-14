#
# @lc app=leetcode id=1441 lang=python3
#
# [1441] Build an Array With Stack Operations
#

# @lc code=start
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res,stack,idx = [],[],0
        for s in range(1,n+1):
            stack.append(s)
            res.append("Push")
            if stack == target:
                return res
            elif stack[idx] == target[idx]:
                idx += 1
            else:
                stack.pop()
                res.append("Pop")
        return res
# @lc code=end

