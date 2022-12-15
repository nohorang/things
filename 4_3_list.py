students = ["신영", "연지", "소민", "채은", "소화", "미나", "민서", "지원"]
grades = [3, 2, 3, 3, 2, 1, 2, 2]
print("students[0]", students[0])
print("len(students)", len(students))
print("min(grades)", min(grades))
print("max(grades)", max(grades))
print("sum(grades)", sum(grades))

import statistics
print("statistics.mean(grades)", statistics.mean(grades))

import random
print("random.choice(students)", random.choice(students))