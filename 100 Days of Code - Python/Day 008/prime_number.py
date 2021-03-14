"""
test if a number is a prime number
"""
def prime_checker(number):
    check = True
    for i in range(2,number):
        if number % i == 0:
            check = False
    print(f"Is the number a prime number? {check}")

n = int(input("Check this number: "))
prime_checker(number=n)