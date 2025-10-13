#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#

# @lc code=start
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        cur = slow
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        p1,p2 = head,prev
        while p2.next:
            temp1, temp2 = p1.next , p2.next
            p1.next = p2
            p2.next = temp1
            p1 , p2 = temp1 , temp2
        
# @lc code=end

