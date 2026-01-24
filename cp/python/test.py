from collections import deque
students = [1,1,1,0,0,1]
d = deque(students)
print(d.pop())
print(d)
print(d.append(7))
print(d)
print(d.popleft())
print(d)
print(d[0])
print(d[-1])
print(d[0])
