#if statemnet 21/11/2024
course = "DataScience"
if course == "DataScience":
    print("You are on the right track!")

    aadesh=9
if aadesh>=7:
    print("Impressive aadesh!")
   
   
    marks=90
    if marks>=90:
        print("you got an A grade")
     

number=79
if number % 2 != 0:
    print("the number is odd")

     

number = 52
if number % 2 == 0:
    print("The number is even.")

    temperature=25
    if temperature<27:
        print("it is a nice weather")
     

temperature = 25
if temperature > 23:
    print("It's a warm day.")

age=18
if age>=18:
    print("you are an adult")
else:
    print("you are not an adult")     

score=75
passing_score=70
if score>=passing_score:
    print("Congratulations,you passed")
else:
    if score >= passing_score - 5:
        print("you almost passed")
    else:
        print("you didnot pass.")

#if-elif-else' Statement

course="datascience"
if course=="datascience":
    print("you are in aadeshs course")
elif course=="physics":
        print("you are in physics wallahs course.")
else:print("you are not enrollrd in any course.")


grades=5

if grades>=7:
    print("impressive skills.")
elif grades>=5:
    print("you are doing well at physice wallah")
else:
    print("keep working on yoour skills.")


marks=75
if marks>=90:
    print("you got an A grade")
elif marks>=80:
    print("you got an B grade")
else:
    print("you got a grade lower than B")     

grade=" "
if grade=="A":
    print("Excellent")
elif grade=="B":
    print("good job")
else:
    print("try harder.")


num=0
if num>=0:
    print("Positive")
elif num<=0:
    print("Negative")
else:
    print("zero")


age=30
if age<18:
    print("you are a minor")
elif 18<=age<65:
    print("you are adult")  
else:
    print("you are senior citizen")   



#if-else' Statement

course="datascience"

if course=="datascience":
    print("you are studing data science")
else:
    print("you are not in the data science course")



aadesh=9

if aadesh>=7:
    print("Impressive aadesh.")
else:
    print("you are making progress at physice wallah")   


is_raining= True
if is_raining:
    print("Take an umbrella.")
else:
    print("enjoy the sunshine.")


num=7
if num%2==0:
    print("even")
else:  
    print("odd")


score=85
result="pass"if score>=70 else "fail" 
print(f"you {result}.")
     

#Nested 'if-else' Statement

course="datascience"
if course=="datascience":
    if grades>=7:
        print("Impressive skills in data science at aadesh!")

marks=88
if marks>=80:
    print("you got an A grade.")        
else :
    print("you got a B grade.")
   
is_weeked= False
is_sunny=True

if is_weeked:
    if is_sunny:
        print("Go for a picnic.")
    else:
        print("stay in and relax.")
else:
    print("it is a workday.")      

     

is_student = True
is_teacher = False

if is_student:
    if is_teacher:
        print("You are both a student and a teacher.")
    else:
        print("You are a student but not a teacher.")
else:
    if is_teacher:
        print("You are a teacher but not a student.")
    else:
        print("You are neither a student nor a teacher.")

is_vip=True
age=30    

if is_vip:
    if age>=18:
       if age<65:
        print("welcome, VIP customer! ")
    else:
        print("You are a VIP but you qualify for senior discounts.")
    print("VIP status is for adults only.")
else:
    print("Regular pricing applies.")

     


     
     