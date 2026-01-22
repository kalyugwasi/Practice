from typing import List
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        stack = [arr[0]]
        res = []
        for a in range(len(arr),1,1):
            if arr[a] > stack[-1]:
                stack.append(arr[a])
                if res[-1] != 1:
                    res.append(1)
            else:
                stack.append(arr[a])
                if res[-1] != 0:
                    res.append(0)
        return res         
sol = Solution()
print(sol.validMountainArray([0,3,2,1]))