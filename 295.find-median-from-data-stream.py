#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#

# @lc code=start
class MedianFinder:

    def __init__(self):
        self.minHeap = []
        heapq.heapify(self.minHeap)
        
    def addNum(self, num: int) -> None:
        heapq.heappush(self.minHeap,num)
        return None

    def findMedian(self) -> float:
        if len(self.minHeap) > 1:
            return float((self.minHeap[0] + self.minHeap[-1])/2)
        else:
            return self.minHeap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

