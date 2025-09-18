# alternatively 
# class Solution:
   # def reverseWords(self, s: str) -> str:
       # return " ".join(s.split()[::-1])

class Solution:
    def reverseWords(self, s: str) -> str:
        liststr =  s.split()
        liststr.reverse()
        return " ".join(liststr)

sol = Solution()
print(sol.reverseWords("the sky is blue"))