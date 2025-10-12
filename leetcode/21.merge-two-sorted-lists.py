#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dum = ListNode(0)
        dumhead = dum
        while list1 and list2:
            if list1.val < list2.val:
                dum.next = list1
                list1 = list1.next
            else:
                dum.next = list2
                list2 = list2.next
            dum = dum.next
        dum.next = list1 or list2
        return dumhead.next
# @lc code=end

