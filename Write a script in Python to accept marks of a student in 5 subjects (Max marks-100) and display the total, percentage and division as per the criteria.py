#Write a script in Python to accept marks of a student in 5 subjects (Max marks-100) and display the total, percentage and division as per the criteria:

sub1=int(input("Enter marks of the first subject: "))

sub2=int(input("Enter marks of the second subject: "))

sub3=int(input("Enter marks of the third subject: "))

sub4=int(input("Enter marks of the fourth subject: "))

sub5=int(input("Enter marks of the fifth subject: "))

avg=(sub1+sub2+sub3+sub4+sub4)/5

if(avg>=60):
    print("1st Division")

elif(avg>=50):
    print("2nd Division")

elif(avg>=40):
    print("3rd Division")

else:
    print("Failed")
