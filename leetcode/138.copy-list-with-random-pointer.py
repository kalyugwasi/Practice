#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        dc = {}
        cur = head
        while cur:
            dc[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            dc[cur].next = dc.get(cur.next)
            dc[cur].random = dc.get(cur.random)
            cur = cur.next
        return dc[head]
        
        
# @lc code=end

