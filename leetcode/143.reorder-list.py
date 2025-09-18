#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#

# @lc code=start

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow ,fast = head , head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        prev = None
        slow.next = None
    
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        #merge
        first ,second = head , prev
        while second:
            temp1, temp2 = first.next , second.next
            first.next = second
            second.next = temp1
            first , second = temp1 , temp2
        
# @lc code=end

