class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        output = [1] * n
        left = 1
        for i in range(n):
            output[i] = left
            left *= nums[i]
        right = 1
        for i in range(n - 1, -1, -1):
            output[i] *= right
            right *= nums[i]
        return output
    
sol = Solution()
print(sol.productExceptSelf([1, 2, 3, 4]))      
print(sol.productExceptSelf([-1, 1, 0, -3, 3])) 
print(sol.productExceptSelf([0, 0]))            

