#
# @lc app=leetcode id=1456 lang=python3
#
# [1456] Maximum Number of Vowels in a Substring of Given Length
#

# @lc code=start
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = 'aeiou'
        l , cnt , res  = 0,0,0
        for r in range(len(s)):
            cnt += 1 if s[r] in vowel else 0
            if r-l +1 >k:
                cnt -= 1 if s[l] in vowel else 0
                l += 1
            res = max(res,cnt)
        return res
        
# @lc code=end

