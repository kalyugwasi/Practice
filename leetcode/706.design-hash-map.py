#
# @lc app=leetcode id=706 lang=python3
#
# [706] Design HashMap
#

# @lc code=start
from collections import defaultdict
class MyHashMap:

    def __init__(self):
        self.res = defaultdict()

    def put(self, key: int, value: int) -> None:
        if key not in self.res:
            self.res[key] = []
        self.res[key] = value            

    def get(self, key: int) -> int:
        if key not in self.res:
            return -1
        else:
            return self.res[key]
    
    def remove(self, key: int) -> None:
        if key in self.res:
            self.res.pop(key)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
# @lc code=end

