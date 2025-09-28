#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l,r=0,0
        while l<len(nums1) and r<len(nums2):
            if nums1[l]!=0:
                l+=1
            else:
                nums1[l] = nums2[r]
                l+=1
                r+=1
        nums1.sort()
# @lc code=end

