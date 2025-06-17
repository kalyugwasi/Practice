class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        len1 = len(flowerbed)
        available = 0
        i = 0
        while i < len1:
            if flowerbed[i] == 0:
                empty_left = (i == 0) or (flowerbed[i-1] == 0)
                empty_right = (i == len1-1) or (flowerbed[i+1] == 0)
                if empty_left and empty_right:
                    flowerbed[i] = 1
                    available += 1
            i += 1
        return n <= available

sol = Solution()
print(sol.canPlaceFlowers([0,1,0],1))