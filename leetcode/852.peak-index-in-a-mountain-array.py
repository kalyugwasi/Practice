#
# @lc app=leetcode id=852 lang=python3
#
# [852] Peak Index in a Mountain Array
#

# @lc code=start
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l,h = 0,len(arr)-1
        while l<h:
            m = l+(h-l)//2
            if arr[m] < arr[m+1]:
                l = m+1
            elif arr[m]>arr[m+1]:
                h = m
        return l
        '''
        arr = [(v,i) for i,v in enumerate(arr)]
        arr.sort(key=lambda x:x[0],reverse=True)
        return arr[0][1]
        '''
# @lc code=end

