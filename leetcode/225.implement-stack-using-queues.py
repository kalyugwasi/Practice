#
# @lc app=leetcode id=225 lang=python3
#
# [225] Implement Stack using Queues
#

# @lc code=start
class MyStack:

    def __init__(self):
        self.dp = deque()

    def push(self, x: int) -> None:
        self.dp.appendleft(x)
        
    def pop(self) -> int:
        return self.dp.popleft()
        
    def top(self) -> int:
        return self.dp[0]

    def empty(self) -> bool:
        return True if not self.dp else False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end

