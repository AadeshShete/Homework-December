print("Assingnment 1")
### Python
#1. What is Python, and why is it widely used in programming?

#Python is a high-level, interpreted programming language.
#It was created by Guido van Rossum and released in 1991.
#It's known for its simplicity and readability.
#Widely used because:
#Easy to learn and use.
#Offers extensive libraries and frameworks.
#Versatile in various fields like web development, data science, AI,machine learning and more.
#Cross-platform: Python works on various operating systems (Windows, Linux, macOS)
#programs written in Python can be run on any platform without modification.
#Community and ecosystem: A large community provides support, tutorials, and third-party packages to extend Python's functionality.


#2. Explain the difference between dynamically typed and statically typed languages. Is Python dynamically or statically typed?

#Dynamically typed languages:
#Type checking occurs at runtime.
#Variables can change type.
#No need to declare variable types.
#Example: Python, JavaScript.

#Statically typed languages:
#Type checking occurs at compile-time.
#Variables' types are fixed when declared.
#Example: C, Java.
#Python is dynamically typed, meaning you don't need to explicitly declare variable types.


### Data Types
#3. List the built-in data types in Python and give an example of each.

#int (Integer): Whole numbers.
#Example: x = 10

#float (Floating-point number): Numbers with decimal points.
#Example: y = 3.14

#str (String): A sequence of characters.
#Example: name = "Aadesh"

#list: An ordered, mutable collection of items.
#Example: fruits = ["apple", "banana", "cherry"]

#tuple: An ordered, immutable collection of items.
#Example: coordinates = (10, 20)

#dict (Dictionary): A collection of key-value pairs.
#Example: person = {"name": "Alice", "age": 25}

#set: An unordered collection of unique items.
#Example: colors = {"red", "blue", "green"}

#bool (Boolean): Represents True or False.
#Example: is_active = True


#4. What is the difference between a list and a tuple in Python? Provide examples.

#Lists:
#Mutable (can change content).
#Defined using square brackets []
#Example: my_list = [1, 2, 3]

#Tuples:
#Immutable (cannot change content).
#Defined using parentheses ()
#Example: my_tuple = (10, 20, 30)


### Basic Conditional Flow

#5. Write a Python program to check if a given number is positive, negative, or zero.

num = float(input("Enter a number: "))

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")

#The program takes a number as input.
#It then checks if the number is greater than zero (positive), less than zero (negative), or equal to zero (zero).


#6. Explain the use of the `if-elif-else` statement in Python with a code example.

#The if-elif-else statement is used to execute different blocks of code based on conditions.
#if: Tests the first condition.
#elif: (else if) Tests additional conditions if the if condition fails.
#else: Executes if none of the above conditions are true.
#Example:

age = 25
if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
else:
    print("Adult")

#The program checks if the person’s age is less than 13, between 13 and 19, or 20 and above, and prints the corresponding category.


### Type Conversion
#7. What is type conversion in Python, and what are the two types of type conversion?

#Type conversion is the process of converting one data type to another.

#Implicit Type Conversion : Python automatically converts one data type to another when needed.
#Example: Adding an integer 

#Explicit Type Conversion: The programmer manually converts a data type using functions like int(), float(), str(), etc.
#Example: x = int("10")


#8. Write a Python program to take user input as a string and convert it into an integer. Handle any potential errors that might occur.

num_str = input("Enter a number: ")
try:
    # Try to convert input to an integer
    num = int(num_str)
    print(f"The number is {num}")
except ValueError:
    # Handle error if conversion fails
    print("Invalid input! Please enter a valid number.")

#The program asks the user to input a value.
#It attempts to convert the input into an integer using the int() function.
#If the input cannot be converted to an integer
#(e.g., the user enters a non-numeric string), the ValueError exception is caught, and an error message is displayed.

