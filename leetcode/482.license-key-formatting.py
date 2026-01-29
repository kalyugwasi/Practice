#
# @lc app=leetcode id=482 lang=python3
#
# [482] License Key Formatting
#

# @lc code=start
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-","").upper()
        res =[]
        while s:
            res.append(s[-k:])
            s = s[:-k]
        return "-".join(res[::-1])

        
# @lc code=end

