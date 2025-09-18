class Solution:
    def possibleStringCount(self, word: str) -> int:
        n = len(word)
        res = 1
        i = 0
        
        while i < n:
            j = i
            while j < n and word[j] == word[i]:
                j += 1
            run_length = j - i
            if run_length > 1:
                res += (run_length - 1)
            i = j
        
        return res
