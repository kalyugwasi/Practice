#
# @lc app=leetcode id=831 lang=python3
#
# [831] Masking Personal Information
#

# @lc code=start
import re
class Solution:
    def maskPII(self, s: str) -> str:
        lis = list(s)
        if '@' in lis:
            before,after,flag = "","",False
            for i in lis:
                if i == '@':
                    flag = True
                elif i != '@' and flag:
                    after += i
                elif i != "@" and not flag:
                    before += i
            before = before[0] +"*"*(5) +before[-1]
            return before.lower()+'@'+after.lower()
        else:
            s = re.sub(r'[+\-() ]', '', s)
            temp = ["***-***-","+*-***-***-","+**-***-***-","+***-***-***-"]
            main = s[-4:]
            n = len(s)
            if n==10:
                return temp[0]+main
            elif n==11:
                return temp[1]+main
            elif n==12:
                return temp[2]+main
            else:
                return temp[3]+main
# @lc code=end

