def my_factorial(number):
    fact = 1
    for x in range(number, 0, -1):
        fact *= x
        print(f"Factorial of {number} is {fact}")

my_factorial(7)
my_factorial(4)
