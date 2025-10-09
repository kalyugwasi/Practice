#
# @lc app=leetcode id=895 lang=python3
#
# [895] Maximum Frequency Stack
#

# @lc code=start
class FreqStack:

    def __init__(self):
        self.stacks = {}
        self.cnt = {}
        self.maxcnt = 0
        
    def push(self, val: int) -> None:
        valcnt = 1 + self.cnt.get(val,0)
        self.cnt[val] = valcnt
        if valcnt > self.maxcnt:
            self.maxcnt = valcnt
            self.stacks[valcnt] = []
        self.stacks[valcnt].append(val)

    def pop(self) -> int:
        res = self.stacks[self.maxcnt].pop()
        self.cnt[res] -= 1
        if not self.stacks[self.maxcnt]:
            self.maxcnt -= 1
        return res 
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
# @lc code=end

