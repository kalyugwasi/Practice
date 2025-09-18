class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        output = []
        max_candies = max(candies)
        for candy in candies:
            output.append(candy + extraCandies >= max_candies)
        return output

sol = Solution()
print(sol.kidsWithCandies([2,3,5,1,3],3))