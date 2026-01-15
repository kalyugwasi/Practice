#
# @lc app=leetcode id=636 lang=python3
#
# [636] Exclusive Time of Functions
#

# @lc code=start
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res,stack,prev_time = [0] * n,[],0
        for log in logs:
            fn, typ, time = log.split(":")
            time = int(time)
            if typ == "start":
                if stack:
                    res[stack[-1]] += time - prev_time
                stack.append(int(fn))
                prev_time = time
            else:
                res[stack.pop()] += time - prev_time + 1
                prev_time = time + 1
        return res
# @lc code=end

