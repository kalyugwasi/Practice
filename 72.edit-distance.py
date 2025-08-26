#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        w1l,w2l = len(word1),len(word2)
        cache = [[float("inf")] * (w2l+1) for i in range(w1l+1)]
        for j in range(w2l+1):
            cache[w1l][j] = w2l - j
        for i in range(w1l+1):
            cache[i][w2l] = w1l - i
        for i in range(w1l-1,-1,-1):
            for j in range(w2l-1,-1,-1):
                if word1[i] == word2[j]:
                    cache[i][j] = cache[i+1][j+1]
                else:
                    cache[i][j] = 1 + min(cache[i+1][j],cache[i][j+1],cache[i+1][j+1])
        return cache[0][0]


        
# @lc code=end

