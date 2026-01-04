#
# @lc app=leetcode id=752 lang=python3
# @lc code=start
import pysnooper
from collections import deque
from typing import List
@pysnooper.snoop()
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        def children(lock):
            res = []
            for i in range(4):
                digit = str((int(lock[i]) + 1) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
                digit = str((int(lock[i]) - 1 + 10) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
            return res

        q,visit = deque(),set(deadends)
        q.append(["0000",0]) #lock,turns
        while q:
            lock,turns = q.popleft()
            if lock == target:
                return turns
            for child in children(lock):
                if child not in visit:
                    visit.add(child)
                    q.append([child,turns+1])
        return -1
sol = Solution()
print(sol.openLock(["0201","0101","0102","1212","2002"],"0202"))

# @lc code=end

