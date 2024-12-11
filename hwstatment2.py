#Find the largest of three numbers
#Given three numbers, find the largest using nested if statements.

num1=int(input("enter the first no:"))
num2=int(input("enter the second no:"))
num3=int(input("enter the third no:"))

if num1>=num2:
    print("first no is large.")
elif num2>=num3:
    print("second no is large.")   
elif num3>=num1:
    print("third no is large.")
else:
    print("it is not")

#enter the first no:3
#enter the second no:2
#enter the third no:1
#first no is large.      

#Check leap year
#Write a program to check if a given year is a leap year or not:
#Divisible by 4 and not 100, or divisible by 400.

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or(year % 400 == 0):
    print(year, "it is a leap year")
else:
    print(year, "it is not a leap year") 

#Enter a year: 2016
#2016 it is a leap year

#Nested temperature check
#Categorize temperature into:
#Cold: Below 15°C
#Warm: 15°C to 30°C
#Hot: Above 30°C

temp = float(input("Enter the temperature in Celsius: "))

if temp < 15:
    print("It's cold.")
elif temp <= 30:
    print("It's warm.")
else:
    print("It's hot.")

#Enter the temperature in Celsius: 13
#It's cold.

#Vowel or consonant
#Check if a given character is a vowel or consonant.

char = input("Enter a character: ")

if char in "aeiouAEIOU":
    print(f"{char} is a vowel.")
else:
    print(f"{char} is a consonant.")

#Enter a character: aadesh
#aadesh is a consonant.

#Driving eligibility
#Check if a person is eligible to drive:
#Must be 18 or older.
#Nested check for possessing a valid license.


num_age=int(input("enter the age:"))

if num_age>=18:
    print("you are eligible to drive.")
elif num_age<=18:
    print("you are not eligbile to drive")
else:
    print("not valid age")  

#enter the age:23
#you are eligible to drive.  