name = input("Enter student's name: ")
roll_no = input("Enter roll number: ")

subjects = [
    "DLD (Digital logic Design)",
    "E.W (Expository Writting)",
    "OOP (Object Oriented Programming)",
    "UHQ-II (Understanding Holy Quran-II)",
    "IOT (Internet of Things - Basics)",
    "I.S (Islamic Studies)",
    "M-II (Mathematics-II - PM)",
]
marks = []
for subj in subjects:
    m = float(input(f"Enter marks for {subj}: "))
    marks.append(m)
num_subjects = len(subjects)
total = sum(marks)
percentage = total / num_subjects

if percentage >= 80:
    grade = "A+"
elif percentage >= 70:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 50:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "F"

failed_subject = any(m < 40 for m in marks)

if failed_subject or percentage < 40:
    result = "Fail"
else:
    result = "Pass"

print("\n MARKSHEET ")
print(f"Name : {name}")
print(f"Roll No : {roll_no}")
for subj, m in zip(subjects, marks):
    print(f"{subj:<38}: {m}")
print(f"Total : {total}")
print(f"Percentage : {percentage:.2f}%")
print(f"Grade : {grade}")
print(f"Result : {result}")
print("--------------")
