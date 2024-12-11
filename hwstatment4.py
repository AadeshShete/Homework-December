#Electricity bill
 #Calculate an electricity bill:


#Usage ≤ 100 units: ₹5/unit
#101-200 units: ₹10/unit
#Above 200 units: ₹15/unit

units=int(input("enter the unit:"))
if units <= 100:
    bill = units * 5
    print("eletricity bill:",bill)
elif units <= 200:
    bill = (100 * 5) + (units - 100) * 10
    print("eletricity bill:",bill)
else:
    bill = (100 * 5) + (100 * 10) + (units - 200) * 15
    print("eletricity bill:",bill)

#enter the unit:300
#eletricity bill: 3000

#Season finder
#Find the season based on the month:
#December-February: Winter
#March-May: Spring
#June-August: Summer
#September-November: Autumn

month=str(input("Enter the month:"))

if month in ["december" or "january" or "february"]:
    print("Winter")
elif month in ["march", "april", "may"]:
    print("Spring")
elif month in ["june", "july", "august"]:
    print("Summer") 
else:
    print("Autumn")
#Enter the month:december
#Winter
#Enter the month:novenber
#Autumn

#Password validation
 #Check if a password meets these conditions:


#At least 8 characters.
#Contains the character '@'.

#password=str(input("enter the password:"))
#int=8
#if password>=8 and '@' in password:
 #   print("Password is valid.")
#else:
#print("Password is not valid.")


#Categorize BMI
 #Categorize Body Mass Index (BMI):


#Below 18.5: Underweight
#18.5 - 24.9: Normal
#25 - 29.9: Overweight
#30 or higher: Obese

bmi=float(input("enter the bmi:"))

if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi <= 24.9:
     print("Normal")
elif 25 <= bmi <= 29.9:
     print("Overweight")
else:
     print("Obese")

#enter the bmi:13
#Underweight

#Character type checker
 #Check if a given character is:
#Alphabet
#Digit
#special character

character=str(input("enter the charater:"))

if character>="A" and character>="z" :
    print("Alphabet")
elif character>="0" and character>="9" :
   print("Digit")
else:
  print("Special Character")

#enter the charater:2
#Digit