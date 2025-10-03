#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n,m=len(s1),len(s2)
        if n > m:
            return False
        d1, d2 = {}, {}
        for char in s1:
            d1[char] = 1 + d1.get(char, 0)
        for char in s2[:n]:
            d2[char] = 1 + d2.get(char, 0)
        if d1 == d2:
            return True
            
        for i in range(n,m):
            left = s2[i - n]
            d2[left] -= 1
            if d2[left] == 0:
                d2.pop(left)

            d2[s2[i]] = 1 + d2.get(s2[i], 0)

            if d1 == d2:
                return True

        return False
# @lc code=end

