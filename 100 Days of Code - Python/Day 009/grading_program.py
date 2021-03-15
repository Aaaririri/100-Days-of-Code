"""
replace the scores with the students grades
"""
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
def student_grades():
    student_grades_dict = {}
    for students in student_scores:
        if student_scores[students] > 90:
            # student_grades_dict[students] ="Outstanding" works too
            student_grades_dict.update({students:"Outstanding"})
        elif student_scores[students] > 80:
            student_grades_dict.update({students:"Exceeds Expectations"})
        elif student_scores[students] > 70:
            student_grades_dict.update({students:"Acceptable"})
        else:
            student_grades_dict.update({students:"fail"})
    return student_grades_dict

    
print(student_grades())