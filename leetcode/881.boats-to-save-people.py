#
# @lc app=leetcode id=881 lang=python3
#
# [881] Boats to Save People
#

# @lc code=start
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l,r=0,len(people)-1
        res=0
        while l<r:
            if people[l]+people[r]<=limit:
                r-=1
                l+=1
                res+=1 
            else :
                r-=1
                res+=1
        if l==r:
            res+=1
        return res
# @lc code=end

