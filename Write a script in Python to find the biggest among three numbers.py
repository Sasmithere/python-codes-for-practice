#Write a script in Python to find the biggest among three number.

num1 = float(input("enter first number :"))
num2 = float(input("enter second number :"))
num3 = float(input("enter third number :"))

if (num1 >= num2):
    if (num1 >= num3):
        largest = num1
elif (num2 >= num1):
    if (num2 >= num3):
        largest = num2
else:
   largest = num3

print("The largest number between",int(num1),",",int(num2),"and",int(num3),"is",int(largest))
