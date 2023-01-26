# Write a script in Python to input a calendar year and to check if it is a leap year or not.

year = int(input("Enter Year: "))

if year % 4 == 0:
    print(year, "is a Leap Year")
elif year % 100 == 0:
    print(year, "is not a Leap Year")
elif year % 400 ==0:
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")


