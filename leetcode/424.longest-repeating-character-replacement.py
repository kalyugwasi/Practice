#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = defaultdict(int)

        l = changes = max_freq = 0

        for c in s:
            counter[c]+=1
            if counter[c] > max_freq:
                max_freq = counter[c]
            elif changes == k:
                counter[s[l]] -= 1
                l += 1
            else:
                changes += 1
        return max_freq + changes
        
# @lc code=end

