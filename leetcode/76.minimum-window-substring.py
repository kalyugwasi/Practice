#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s) , len(t)
        have , need = 0 , n
        window , tchar = {} , {}
        if n>m or not s or not t or s == "" or t == "":
            return ""
        res , resl = [-1,-1], float("infinity")
        l = 0
        for char in t:
            tchar[char] = tchar.get(char,0) + 1
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c,0) + 1
            if c in tchar and window[c] <= tchar[c]:
                have += 1
            while have == need:
                if (r-l+1) < resl:
                    res=[l,r]
                    resl = r-l+1
                window[s[l]] -= 1
                if s[l] in tchar and window[s[l]] < tchar[s[l]]:
                    have -= 1
                l += 1
        l,r = res
        return s[l:r+1] if  resl != float("infinity") else "" 
# @lc code=end

