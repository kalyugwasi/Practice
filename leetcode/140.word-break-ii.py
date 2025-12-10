#
# @lc app=leetcode id=140 lang=python3
#
# [140] Word Break II
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n=len(s)
        def bt(i):
            if i == n:
                return [""]
            res = []
            for j in range(i,n):
                word = s[i:j+1]
                if word not in wordDict:
                    continue
                strings = bt(j+1)
                if not strings:
                    continue
                for sub in strings:
                    sentence = word
                    if sub:
                        sentence += " " + sub
                    res.append(sentence)
            return res
        return bt(0)
# @lc code=end

