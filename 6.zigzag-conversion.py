#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = numRows
        if n == 1:
            return s
        res = ["" for _ in range(n)]
        i = 0
        while i < len(s):
            for zig in range(n):
                if i >= len(s):
                    break
                res[zig] += s[i]
                i += 1
            for zag in range(n - 2, 0, -1):
                if i >= len(s):
                    break
                res[zag] += s[i]
                i += 1
        return "".join(res)

# @lc code=end

