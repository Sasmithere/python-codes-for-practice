#Write a script in Python to input the values of principal amount, rate of interest and time from user and compute the simple interest

p=float(input("Enter the Principle Amount :"))

r=float(input("Enter the rate of interest :"))

t=float(input("Enter the time(in years) :"))

S=p * r * t /100

print("Your simple interest (S.I) is ",S)

