student_scores = {
    "Harry":88,
    "Ron": 78,
    "Hermione": 95,
    "Draco": 75,
    "Neville": 60
}
student_grades = {}
for student, nota in student_scores.items():
    if nota >= 90:
        student_grades[student,nota] = "Outstanding"
    elif nota >= 80:
        student_grades[student,nota] = "Exceeds Expectations"
    elif nota >= 70:
        student_grades[student,nota] = "Acceptable"
    else:
        student_grades[student,nota] = "Fail"
print(student_grades)