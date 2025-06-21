#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = ''.join(c for c in s.lower() if c.isalnum())
        left, right = 0, len(strs) - 1
        while left < right:
            if strs[left] != strs[right]:
                return False
            left += 1
            right -= 1
        return True

