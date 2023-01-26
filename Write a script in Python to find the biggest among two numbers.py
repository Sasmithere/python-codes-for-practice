#Write a script in Python to find the biggest among two number.

num1 = float(input("enter first number :"))
num2 = float(input("enter second number :"))


if (num1 >= num2):
    largest = num1
elif (num2 >= num1):
    largest = num2


print("The largest number between",int(num1),",",int(num2),"is",int(largest))
