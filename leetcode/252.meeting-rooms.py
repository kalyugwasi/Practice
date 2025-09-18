from typing import List

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        
        intervals.sort(key=lambda i: i.start)
        prev = intervals[0]
        
        for i in range(1, len(intervals)):
            curr = intervals[i]
            if curr.start < prev.end:
                return False
            prev = curr
        
        return True
