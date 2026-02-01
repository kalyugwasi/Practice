#
# @lc app=leetcode id=686 lang=python3
#
# [686] Repeated String Match
#

# @lc code=start
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        n = a
        count = 1
        while len(n) < len(b):
            n += a
            count += 1
            if b in n:
                return count
        if b in n:
            return count
        n += a
        count += 1
        if b in n:
            return count
        return -1
# @lc code=end

