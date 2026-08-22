#
# @lc app=leetcode id=532 lang=python3
#
# [532] K-diff Pairs in an Array
#

# @lc code=start
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        cnt = Counter(nums)
        res = 0
        for key in cnt.keys():
            if k == 0:
                if cnt[key]>1: res += 1
                continue 
            if key+k in cnt: res += 1
        return res
        
# @lc code=end

