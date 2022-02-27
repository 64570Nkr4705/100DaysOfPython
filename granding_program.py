student_scores = {
    "Harry":81, 
    "Ron":78, 
    "Hermione":99, 
    "Draco":74, 
    "Neville":62,
    }

grade_scores = {}

for key in student_scores:
    if student_scores[key] >= 91:
        grade_scores[key] = "Outslanding"
    elif student_scores[key] < 90 and student_scores[key] >= 81:
        grade_scores[key] = "Exceeds Expectations"
    elif student_scores[key] < 80 and student_scores[key] >= 71:
        grade_scores[key] = "Acceptable"
    else:
        grade_scores[key] = "Fail"

print(grade_scores)
print(student_scores)
