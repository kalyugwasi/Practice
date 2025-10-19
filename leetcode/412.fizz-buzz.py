#
# @lc app=leetcode id=412 lang=python3
#
# [412] Fizz Buzz
#

# @lc code=start
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for i in range(1, n+1):
            fizz = i%3 == 0
            buzz = i%5 == 0

            if fizz and buzz:
                answer.append('FizzBuzz')
            elif fizz:
                answer.append('Fizz')
            elif buzz:
                answer.append('Buzz')
            else:
                answer.append(str(i))
        return answer  
# @lc code=end

