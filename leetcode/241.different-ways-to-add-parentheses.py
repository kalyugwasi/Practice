#
# @lc app=leetcode id=241 lang=python3
#
# [241] Different Ways to Add Parentheses
#

# @lc code=start
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        ops = {
            "+": lambda x, y : x  + y
            "-": lambda x, y : x - y
            "*": lambda x, y : x * y
        }
        def backtrack(left,right):
            res = []
            for i in range(left,right+1):
                op = expression[i]
                if op in ops:
                    num1 = backtrack(left,i-1)
                    num2 = backtrack(i+1,right)
                    for n1 in num1:
                        for n2 in num2:
                            res.append(ops[op](n1,n2))
            if not res: res += [expression[left:right+1]]
            return res
        return backtrack(0,len(expression)-1)
        
# @lc code=end

