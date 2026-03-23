#
# @lc app=leetcode id=818 lang=python3
#
# [818] Race Car
#

# @lc code=start
from collections import deque
class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(0,0,1)])
        visit = set()
        while queue:
            moves,pos,speed  = queue.popleft()
            if pos == target:
                return moves
            if (pos,speed) in visit:
                continue
            else:
                visit.add((pos,speed))
                queue.append((moves+1,pos+speed,speed*2))
                if (pos+speed > target and speed >0) or (pos+speed < target and speed<0):
                    speed = -1 if speed>0 else 1
                    queue.append((moves+1,pos,speed))

# @lc code=end

