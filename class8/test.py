student_scores = [40, 40, 35, 70, 30, 41, 90]

passed = 0

for score in student_scores:
    if score <= 40:
        passed += score

print(passed)