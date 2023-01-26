#Write a script in Python to print first n-even numbers.

n = int(input("Enter a Number : "))
print()
print("The even Numbers from 2 to",n,"are")
for i in range(2,n,2):
    print(i)
    print("")
