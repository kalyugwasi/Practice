#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # Needed for heap comparison
    def __lt__(self, other):
        return self.val < other.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        # Push the head node of each list into the heap
        for node in lists:
            if node:
                heapq.heappush(heap, node)

        dummy = ListNode()
        tail = dummy

        while heap:
            node = heapq.heappop(heap)
            tail.next = node
            tail = tail.next
            if node.next:
                heapq.heappush(heap, node.next)

        return dummy.next

# Helper: Convert list to linked list
def build_linked_list(arr):
    dummy = ListNode()
    curr = dummy
    for num in arr:
        curr.next = ListNode(num)
        curr = curr.next
    return dummy.next

# Helper: Print linked list
def print_linked_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# Example usage:
sol = Solution()
input_lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
linked_lists = [build_linked_list(l) for l in input_lists]
merged = sol.mergeKLists(linked_lists)
print_linked_list(merged)
       
# @lc code=end

