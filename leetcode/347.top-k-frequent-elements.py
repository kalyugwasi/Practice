#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#
# https://leetcode.com/problems/top-k-frequent-elements/description/
#
# algorithms
# Medium (64.56%)
# Likes:    18344
# Dislikes: 731
# Total Accepted:    2.9M
# Total Submissions: 4.4M
# Testcase Example:  '[1,1,1,2,2,3]\n2'
#
# Given an integer array nums and an integer k, return the k most frequent
# elements. You may return the answer in any order.
# 
# 
# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:
# Input: nums = [1], k = 1
# Output: [1]
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
# 
# 
# 
# Follow up: Your algorithm's time complexity must be better than O(n log n),
# where n is the array's size.
# 
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        occ = {}
        answer = []
        for count in nums:
            occ[count] = occ.get(count, 0) + 1
        for _ in range(k):
            key = max(occ, key=occ.get)
            answer.append(key)
            del occ[key]
        return answer
 
sol = Solution()
print(sol.topKFrequent([1,1,1,3,2,2],2))
# @lc code=end

