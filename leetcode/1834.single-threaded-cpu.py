#
# @lc app=leetcode id=1834 lang=python3
#
# [1834] Single-Threaded CPU
#

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i,t in enumerate(tasks):
            t.append(i)
        tasks.sort(key=lambda t : t[0])
        res,minHeap = [],[]
        i, time= 0, tasks[0][0]
        while minHeap or i<len(tasks):
            while i<len(tasks) and time>=tasks[i][0]:
                heapq.heappush(minHeap,(tasks[i][1],tasks[i][2]))
                i+=1
            if not minHeap:
                time = tasks[i][0]
            else:
                proc,index = heapq.heappop(minHeap)
                time += proc
                res.append(index)
        return res
# @lc code=end

