class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ["a","e","i","o","u","A","E","I","O","U"]
        length = len(s)
        vowlesINs = []
        lost_letters = []
        new_str = []
        for element in s:
            if element in vowels:
                vowlesINs.append(element)
            else: lost_letters.append(element)
        vowlesINs.reverse()
        for element in s:
            if element in vowels:
                new_str.append(vowlesINs.pop(0))
            else: new_str.append(element)
        return "".join(new_str) 

sol= Solution()
print(sol.reverseVowels("IceCreAm"))