students_heights = list(map(int, input("Insert here a list of students heights separated bu',': ").split(",")))
total = 0
amount = 0
for students in students_heights:
    total += students
    amount += 1


print(f" The avarege height is: {round(total/amount)}")