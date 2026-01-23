#
# @lc app=leetcode id=1700 lang=python3
#
# [1700] Number of Students Unable to Eat Lunch
#

# @lc code=start
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        d = deque(students)
        sandwiches = deque(sandwiches)
        failed = 0
        while d and failed < len(students):
            if sandwiches[0] == d[0]:
                d.popleft()
                failed = 0
                sandwiches.popleft()
            else:
                failed += 1
                d.append(d.popleft())
        return len(d)
# @lc code=end

