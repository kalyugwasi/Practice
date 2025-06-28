# Given dictionary
student_grades = {"Alice": 85, "Bob": 72, "Charlie": 90, "David": 65, "Eva": 88, "John": 45}

# Complete the code 
import sys
t = "Bob"
if t in student_grades.keys():
    a = student_grades[t]
    print(a)
else: print("Not Found")