#Write a script in Python to print first n-odd numbers in descending order.

n = int(input("Enter Number :"))

for i in range(n - 1, -1, -1):
    a = 1 + i * 2
    print()
    print(a)
