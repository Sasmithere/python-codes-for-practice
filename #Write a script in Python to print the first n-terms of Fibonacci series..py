#Write a script in Python to print the first n-terms of Fibonacci series.

n = int(input("How many terms? : "))

n1 = 0

n2 = 1

count = 0

if n <= 0:
   print("Please enter a positive integer")

elif n == 1:
   print("Fibonacci sequence upto",n,":")

   print()

   print(n1)

else:
   print("Fibonacci sequence upto",n,":")

   while count < n:

       print(n1,end=' ')

       nth = n1 + n2

       n1 = n2

       n2 = nth

       count += 1

