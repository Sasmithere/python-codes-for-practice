#Write a script in Python to print first n-perfect squares.

import math

number = int(input("Enter a Number : "))

root = math.sqrt(number)
if int(root + 0.5) ** 2 == number:
    print(number, "is a perfect square")
else:
    print(number, "is not a perfect square")
