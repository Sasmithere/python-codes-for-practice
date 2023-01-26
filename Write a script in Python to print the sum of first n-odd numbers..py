#Write a script in Python to print the sum of first n-even numbers.

n=int(input('Enter a odd number :'))
i=1
sum=0
while i<n:
    if i%2!=0:
        sum=sum+i
    i+=1
print('Sum of odd numbers',sum)
