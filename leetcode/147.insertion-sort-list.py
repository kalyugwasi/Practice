#
# @lc app=leetcode id=147 lang=python3
#
# [147] Insertion Sort List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dum = ListNode(0,head)
        prev,cur = head,head.next
        while cur:
            if cur.val >= prev.val:
                prev,cur = cur,cur.next
                continue
            tmp = dum
            while cur.val > tmp.next.val:
                tmp = tmp.next
            prev.next = cur.next
            cur.next = tmp.next
            tmp.next = cur
            cur = prev.next
        return dum.next         
# @lc code=end

