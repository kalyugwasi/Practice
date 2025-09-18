class Solution:
    def encode(self, strs: list[str]) -> str:
        encodedString = ""
        for word in strs:
            encodedString += str(len(word)) + '#' + word
        return encodedString
    def decode(self, s: str) -> list[str]:
        strs , i = [] , 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            strs.append(s[j+1:j+1+length])
            i = j + 1 + length
        return strs

sol = Solution()

encoded = sol.encode(["neet", "code", "love", "you"])
print(encoded)

decoded = sol.decode(encoded)
print(decoded)
