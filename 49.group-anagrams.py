#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
# https://leetcode.com/problems/group-anagrams/description/
#
# algorithms
# Medium (70.92%)
# Likes:    20584
# Dislikes: 695
# Total Accepted:    3.8M
# Total Submissions: 5.4M
# Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
#
# Given an array of strings strs, group the anagrams together. You can return
# the answer in any order.
# 
# 
# Example 1:
# 
# 
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# 
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# 
# Explanation:
# 
# 
# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form
# each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to
# form each other.
# 
# 
# 
# Example 2:
# 
# 
# Input: strs = [""]
# 
# Output: [[""]]
# 
# 
# Example 3:
# 
# 
# Input: strs = ["a"]
# 
# Output: [["a"]]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= strs.length <= 10^4
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.
# 
# 
#

# @lc code=start
#class Solution:
#    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
#        listy = []
#        mau = []
#        result = []
#        for i in range(len(strs)):
#            char_count = {}
#            for char in str(strs[i]):
#                char_count[char] = char_count.get(char, 0) + 1
#            listy.append(char_count)
#        for i in range(len(listy)):
#            answer = []
#            for j in range(i+1,len(listy)):
#                if listy[i] == listy[j]:
#                    if strs[i] not in result:
#                        answer.append(strs[i])
#                        result.append(strs[i])
#                        answer.append(strs[j])
#                        result.append(strs[j])
#                    elif strs[j] not in result:
#                        answer.append(strs[j])
#                        result.append(strs[j])
#            if strs[i] not in result:
#                result.append(strs[i])
#                answer.append(strs[i])
#            if answer != []:
#                mau.append(answer)
#        return mau

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = defaultdict(list)
        
        for word in strs:
            # Sort the word and use it as the key
            key = ''.join(sorted(word))
            anagrams[key].append(word)
        
        return list(anagrams.values())

sol = Solution()
print(sol.groupAnagrams(["act","pots","tops","cat","stop","hat"]))
        
# @lc code=end

