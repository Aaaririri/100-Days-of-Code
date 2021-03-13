"""
Is possible to sove it usin the max function, but it is a for loop challenge after all
"""
students_scores = list(map(int, input("Insert here a list of students scores separated bu',': ").split(",")))
max_score = 0
for score in students_scores:
    if max_score < score:
        max_score = score


print(f"The highest score is: {max_score}")
