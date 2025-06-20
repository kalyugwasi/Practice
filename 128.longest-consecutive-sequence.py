#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
        sortedList = sorted(set(nums))
        max_counter = 0
        counter = 1
        for i in range(1, len(sortedList)):
            if sortedList[i] == sortedList[i-1] + 1:
                counter += 1
            else:
                max_counter = max(max_counter, counter)
                counter = 1
        return max(max_counter, counter)
            
sol = Solution()
print(sol.longestConsecutive([100,4,200,1,3,2]))
print(sol.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
        
# @lc code=end

