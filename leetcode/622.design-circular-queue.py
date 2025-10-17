#
# @lc app=leetcode id=622 lang=python3
#
# [622] Design Circular Queue
#

# @lc code=start
<<<<<<< HEAD
class ListNode:
    def __init__(self,prev,val,next):
        self.prev,self.val,self.next = prev,val,next 

class MyCircularQueue:
    def __init__(self, k: int):
        self.space = k
        self.left = ListNode(None,0,None)
        self.right = ListNode(self.left,0,None)        
        self.left.next = self.right

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            cur = ListNode(self.right.prev,value,self.right)
            self.right.prev.next = cur
            self.right.prev = cur
            self.space -= 1
            return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.left.next = self.left.next.next
            self.left.next.prev = self.left
            self.space +=1
            return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.left.next.val
        
    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.right.prev.val

    def isEmpty(self) -> bool:
        return self.left.next == self.right

    def isFull(self) -> bool:
        return self.space == 0

=======
class MyCircularQueue:
    def __init__(self, k: int):
        self.queue = deque()
        self.coun = k
    def enQueue(self, value: int) -> bool:
        if self.coun > 0:
            self.coun -= 1
            self.queue.append(value)
            return True
        else:
            return False
    def deQueue(self) -> bool:
        if self.isEmpty() == True:
            return False
        else:
            self.coun += 1
            self.queue.popleft()
            return True
    def Front(self) -> int:
        return self.queue[0] if not self.isEmpty() else -1
    def Rear(self) -> int:
        return self.queue[-1] if not self.isEmpty() else -1
    def isEmpty(self) -> bool:
        return len(self.queue) == 0
    def isFull(self) -> bool:
        return True if self.coun == 0 else False
        
>>>>>>> 81cf9fb5e68270650597d5a43b1b3501335f39eb

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
<<<<<<< HEAD
=======

>>>>>>> 81cf9fb5e68270650597d5a43b1b3501335f39eb
# @lc code=end

