#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        a , b = nums1 , nums2
        if len(a) > len(b):
            a , b = b , a
        total = len(nums1) + len(nums2)
        half = total // 2
        l , r = 0 , len(a)-1
            


sol = Solution()
print(sol.findMedianSortedArrays(nums1 = [1,3], nums2 = [2]))
print(sol.findMedianSortedArrays(nums1 = [1,2], nums2 = [3,4]))       
# @lc code=end
