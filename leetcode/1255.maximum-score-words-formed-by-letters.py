#
# @lc app=leetcode id=1255 lang=python3
#
# [1255] Maximum Score Words Formed by Letters
#

# @lc code=start
class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        cnt = Counter(letters)
        for i, ch in enumerate("abcdefghijklmnopqrstuvwxyz"):
            if ch in cnt:
                cnt[ch] = [cnt[ch],score[i]]    
        def formable(w):
            wor = Counter(w)
            for c in wor.keys():
                if c not in cnt or wor[c] > cnt[c][0]:
                    return False
            return True
        def back(i):
            if i == len(words):
                return 0
            res = back(i+1)
            if formable(words[i]):
                cur = 0
                for c in words[i]:
                    cnt[c][0] -= 1
                    cur += cnt[c][1]
                res = max(res,cur + back(i+1))
                for c in words[i]:
                    cnt[c][0] += 1
            return res
        return back(0)
# @lc code=end

