#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self):
        self.sucessor = None

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == 1:
            return self.reverseN(head, right)
        head.next = self.reverseBetween(head.next, left-1, right-1)
        return head
        
    def reverseN(self, head, n):
        if n == 1:
            self.sucessor = head.next
            return head
        
        last_in_reverse = self.reverseN(head.next, n-1)
        #reverse pointers
        head.next.next = head
        head.next = self.sucessor
        return last_in_reverse
# @lc code=end

