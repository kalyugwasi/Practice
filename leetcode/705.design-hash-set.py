#
# @lc app=leetcode id=705 lang=python3
#
# [705] Design HashSet
#

# @lc code=start
class MyHashSet:

    def __init__(self):
        self.res = set()

    def add(self, key: int) -> None:
        self.res.add(key)

    def remove(self, key: int) -> None:
        if key in self.res:
            self.res.remove(key)
        else:
            return False        

    def contains(self, key: int) -> bool:
        if key in self.res:
            return True
        return False 
      


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
# @lc code=end

