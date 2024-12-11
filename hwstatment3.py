#Triangle validation
# Check if three sides can form a triangle:
#The sum of any two sides must be greater than the third side.

side1=int(input("enter the first side:"))
side2=int(input("enter the second side:"))
side3=int(input("enter the third side:"))

if side1+side2>side3 and side1+side3>side2 and side2+side3>side1:
  print("The sides can form a triangle.")
else:
  print("The sides cannot form a triangle.")

#enter the first side:5
#enter the second side:3
#enter the third side:7
#The sides can form a triangle.


#Calculate tax based on salary
# Determine the tax rate:
#Salary ≤ 5,00,000: 5%
#5,00,001 - 10,00,000: 10%
#bove 10,00,000: 20%

num_tax=int(input("enter the salary:"))
if num_tax<= 500000:
    print("tax rate is 5%")
elif num_tax>= 500001 or num_tax<= 1000000:
    print("tax rate is 10%")
elif num_tax>= 1000000:
    print("tax rate is 20%")
else:
   print("not valid")

#enter the salary:500001
#tax rate is 10%


#Categorize age
#Categorize a person's age:
#0-12: Child
#13-19: Teen
#20-59: Adult
#60+: Senior

age=int(input("enter the age:"))

if age<=12:
    print("Child")
elif age<=19:
    print("Teen")
elif age<=59:
    print("Adult")
elif age>=60:
    print("Senior")
else:
    print("not valid")

#enter the age:79
#Senior

#Logical AND check
 #Check if a number is greater than 10 and divisible by 2.

num=int(input("enter the no:"))
if num > 10 and num % 2 == 0:
   print("no is greater than 10 and divisible by 2")
else:
   print("no is not grather than 10 or not divisible by 2")   

#enter the no:14
#no is greater than 10 and divisible by 2

#Logical OR check
 #Check if a number is less than 5 or greater than 20.

number=int(input("enter the no:"))
if number < 5 or number > 20:
    print(number, "is less than 5 or greater than 20.")
else:
  print(number, "is not less than 5 and not greater than 20.")

#enter the no:25
#25 is less than 5 or greater than 20.