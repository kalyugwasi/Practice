#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#
# https://leetcode.com/problems/valid-anagram/description/
#
# algorithms
# Easy (66.65%)
# Likes:    13094
# Dislikes: 434
# Total Accepted:    4.8M
# Total Submissions: 7.3M
# Testcase Example:  '"anagram"\n"nagaram"'
#
# Given two strings s and t, return true if t is an anagram of s, and false
# otherwise.
# 
# 
# Example 1:
# 
# 
# Input: s = "anagram", t = "nagaram"
# 
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: s = "rat", t = "car"
# 
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length, t.length <= 5 * 10^4
# s and t consist of lowercase English letters.
# 
# 
# 
# Follow up: What if the inputs contain Unicode characters? How would you adapt
# your solution to such a case?
# 
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        char_count_t = {}
        char_count_s = {}
        for char in s:
            char_count_s[char] = char_count_s.get(char, 0) + 1
        for char in t:
            char_count_t[char] = char_count_t.get(char, 0) + 1
        return char_count_s == char_count_t
        


# @lc code=end

