#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        maxstr = []
        l , r = 0 , 1
        while l < len(s):
            maxstr.append(list(s[l]))
            if list(s[r]) not in maxstr:
                maxstr.append(list(s[r]))
                r += 1
                length = max(length , len(maxstr))
            else:
                maxstr.append(list(s[r]))
                maxstr.pop(0)
                l = r+1
        print(length)
sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb")) 
        
# @lc code=end

