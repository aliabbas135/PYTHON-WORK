total = 0
num_subjects = 5

for i in range(1, num_subjects + 1):
    marks = float(input(f"Enter marks for subject {i} (out of 100): "))
    total += marks

percentage = total / num_subjects

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

result = "Pass" if percentage >= 50 else "Fail"

print(f"\nTotal Marks: {total}")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")
print(f"Result: {result}")
