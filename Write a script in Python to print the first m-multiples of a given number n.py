#Write a script in Python to print the first m-multiples of a given number n

x=int(input("Enter a number : "))

m=int(input("Enter value for multiples : "))

for i in range(1,m):
    print(i*x)
