#
# @lc app=leetcode id=682 lang=python3
#
# [682] Baseball Game
#

# @lc code=start
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        rec = deque()
        for op in operations:
            if op == "C":
                rec.pop()
            elif op == "D":
                rec.append(2 * rec[-1])
            elif op == "+":
                rec.append(rec[-1] + rec[-2])
            else:
                rec.append(int(op))
        return sum(rec)
# @lc code=end

