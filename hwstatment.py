#hw on struture 21\11\2024
#Check a number
#Write a program to check if a number is positive, negative, or zero.

num=int(input("enter the no:"))

if num>0:
    print("The no is positive")
elif num<0:
    print("The no is negative")
else:
    print("The no is zero")


#Enter a no: 79
#The no is positive

#Enter a no: -78
#The no is negative

#Enter a n0: 0
#The no is zero

#Check even or odd
#Write a program to check if a given number is even or odd.

num = int(input("enter a no:"))

if num % 2 == 0:
    print("The no is even.")
else:
    print("The no is odd.")

#enter a no:79
#The no is odd.

#enter a no:78
#The no is even.

#Check divisibility
 #Check if a given number is divisible by 3, 5, or both.

num=int(input("Enter the no:"))

if num%3==0 and num%5==0:
    print("the no is divisible by both 3 and 5")
elif num%3==0:
    print("the no is divisible by 3")
elif num%5==0:
    print("the no is divisible by 5")
else:
    print("the no is  not divisible by both 3 and 5")

#Enter the no:15
#the no is divisible by both 3 and 5

#Enter the no:7 
#the no is  not divisible by both 3 and 5

#Minimum of two numbers
 #Find the smaller number between two given numbers.

num1 = int(input("Enter the first no: "))
num2 = int(input("Enter the second no: "))

if num1 < num2:
    small_num = num1
else:
    small_num = num2

print("The smaller number is:",small_num)

#Enter the first no: 18
#Enter the second no: 16
#The smaller number is: 16

#Grade Checker
 #Write a program to display grades based on a percentage:
#A: 90-100
#B: 70-89
#C: 50-69
#F: Below 50

percent = int(input("Enter the percentage: "))

if percent >= 90:
    print("grade = A")
elif percent >= 70:
    print("grade = B")
elif percent >= 50:
    print("grade = C")
else:
    print("grade = F")

#Enter the percentage: 97
#grade = A
