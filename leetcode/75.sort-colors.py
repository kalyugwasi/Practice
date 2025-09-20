#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
class Solution:
    def swap(self,nums,i,j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
    def sortColors(self, nums: List[int]) -> None:
        l,i,r=0,0,len(nums)-1
        while i<=r:
            if nums[i]==0:
                self.swap(nums,l,i)
                l+=1
            elif nums[i] == 2:
                self.swap(nums,i,r)
                r-=1
                i-=1
            i+=1
        
# @lc code=end

