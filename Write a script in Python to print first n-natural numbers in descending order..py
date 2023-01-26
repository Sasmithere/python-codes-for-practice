#Write a script in Python to print first n-natural numbers in descending order.

n = int(input("Enter Number :"))

for i in range(n - 1, -1, -1):
    a = 1 + i
    print()
    print(a)
