#
# @lc app=leetcode id=698 lang=python3
#
# [698] Partition to K Equal Sum Subsets
#

# @lc code=start
class Solution:
    def canPartitionKSubsets(self, N: List[int], k: int) -> bool:
        n,side = len(N), sum(N)/k
        N.sort(reverse=True)
        if side != int(side) or N[0] > side:
            return False
        def btrack(i,space,done):
            if done == k:
                return True
            while i<n:
                num = N[i]
                if num > space:
                    i += 1
                    continue
                N[i] = side + 1
                if num == space:
                    res = btrack(1,side,done+1)
                else:
                    res = btrack(i+1,space-num,done)
                if res:
                    return True
                N[i] = num
                while i < n and N[i] == num:
                    i += 1                
            return False 
        return btrack(0,side,0)
# @lc code=end

