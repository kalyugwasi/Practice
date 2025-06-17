class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        count_1 = flowerbed.count(1)
        len1 = len(flowerbed)
        possible_len = 0
        if len1 % 2 == 0:
            possible_len = len1/2
        else: possible_len = round((len1+1)/2)
        available = possible_len - count_1
        if n <= available:
            return True
        else: return False

sol = Solution()
print(sol.canPlaceFlowers([1,0,0,0,1],2))