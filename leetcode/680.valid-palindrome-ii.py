#
# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str,allo = 1) -> bool:
        if s == s[::-1]:
            return True
        else:
            left,right=0,len(s)-1
            while left<right:
                if s[left] == s[right]:
                    left += 1
                    right -=1
                else:
                    if allo <1:
                        return False
                    else:
                        remL = self.validPalindrome(s[:left]+s[left+1:],0)
                        remR = self.validPalindrome(s[:right]+s[right+1:],0)
                        if remL == False and remR == False:
                            return False
                        else:
                            return True
        return True
                        

                

                
# @lc code=end

