#
# @lc app=leetcode id=229 lang=python3
#
# [229] Majority Element II
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        le = len(nums)
        freq = Counter(nums)
        for k,v in freq.items():
            if v>(le//3):
                res.append(k)
        return res
# @lc code=end

