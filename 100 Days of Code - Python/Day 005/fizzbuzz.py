"""
if divisible by 3 Fizz
if divisible by 5 Buzz
if divisible by 3 and 5 FizzBuzz
"""
for num in range(1, 101):
    if num % 15 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)


