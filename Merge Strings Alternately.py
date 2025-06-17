class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_word = ""
        i = 0
        while i < len(word1) or i < len(word2):
            if i < len(word1):
                new_word += word1[i]
            if i < len(word2):
                new_word += word2[i]
            i += 1
        return new_word

sol = Solution()
print(sol.mergeAlternately("abc", "pqr"))