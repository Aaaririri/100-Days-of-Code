"""
Calculate the sum of all even numbers between[1,100]
"""
s = 0
for num in range(2, 101, 2):
    s += num


print(f"The sum of all even numbers between 1 and 100 is: {s}")