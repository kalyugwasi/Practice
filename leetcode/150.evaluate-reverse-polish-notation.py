#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        self.stack = []
        operator = ['+', '-', '*', '/']
        for val in tokens:
            if val not in operator:
                self.stack.append(int(val))
            else:
                b = self.stack.pop()
                a = self.stack.pop()
                if val == '+':
                    self.stack.append(a + b)
                elif val == '-':
                    self.stack.append(a - b)
                elif val == '*':
                    self.stack.append(a * b)
                elif val == '/':
                    self.stack.append(int(a / b))
        return self.stack[0]
sol = Solution()
print(sol.evalRPN(["2","1","+","3","*"]))
# @lc code=end

