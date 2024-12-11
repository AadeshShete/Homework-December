#Here are some commonly asked Python interview questions along with guidance on how to answer them:

### 1. What are Python’s key features?
#Answer:
#Python is popular because of its:
#- Ease of use: Simple and beginner-friendly syntax.
#- Portability: Python programs run on different platforms (Windows, MacOS, Linux) without modification.
#- Extensive libraries: Includes libraries for tasks like web development (Django), data analysis (pandas, NumPy), and machine learning (TensorFlow).
#- Interpreted and dynamically typed: No need to declare variables; types are checked at runtime.
#- Object-oriented: Supports object-oriented programming for building reusable code.

#Example Follow-Up Tip: Mention specific libraries you have used.


### 2. Explain Python’s Global Interpreter Lock (GIL).
#Answer:
#The Global Interpreter Lock (GIL) is a mutex that protects access to Python objects, ensuring only one thread executes Python bytecode at a time. It simplifies memory management in CPython but limits the performance of multi-threaded Python programs.

#Example Follow-Up Tip: Explain that GIL is why Python’s multiprocessing is often preferred over multithreading for CPU-bound tasks.


### 3. What are Python decorators?
#Answer:
#Decorators are a way to modify or extend the behavior of functions or methods. They are implemented as callable objects that take a function as input and return a modified or new function.

#Example:
def decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello()

#Output:
#Before function call
#Hello!
#After function call

#Example Follow-Up Tip: Mention a real-world use, like logging, authentication, or memoization.


### 4. Differentiate between deep copy and shallow copy.
#Answer:
#- Shallow Copy: Creates a new object but copies only references to the original objects' elements.
#- Deep Copy: Creates a new object and recursively copies all objects inside the original object.

#Example:
import copy

original = [[1, 2], [3, 4]]
shallow = copy.copy(original)
deep = copy.deepcopy(original)

shallow[0][0] = 99
deep[1][0] = 88

print(original)  # Output: [[99, 2], [3, 4]]
print(deep)      # Output: [[1, 2], [88, 4]]


### 5. Explain Python’s memory management.
#Answer:
#Python manages memory using:
#1. Reference counting: Tracks how many references point to an object.
#2. Garbage collection: Reclaims memory for objects no longer referenced using cyclic garbage collectors.

#Example Follow-Up Tip: Mention how del can remove an object reference and trigger garbage collection.


### 6. What is the difference between `is` and `==` in Python?
#Answer:
#- == checks value equality (if two objects have the same value).
#- is checks identity equality (if two objects are the same in memory).

#Example:
a = [1, 2]
b = [1, 2]

print(a == b)  # True (values are the same)
print(a is b)  # False (different memory locations)


### 7. How does Python handle mutable and immutable objects?
#Answer:
#- Mutable objects: Can be modified after creation (e.g., lists, dictionaries).
#- Immutable objects: Cannot be modified after creation (e.g., strings, tuples).

#Example:
# Mutable
list_a = [1, 2, 3]
list_a[0] = 99
print(list_a)  # Output: [99, 2, 3]

# Immutable
tuple_a = (1, 2, 3)
# tuple_a[0] = 99  # Raises TypeError


### 8. What are Python’s data types?
#Answer:
#- Numeric: int, float, complex
#- Sequence: list, tuple, range
#- Text: str
#- Mapping: dict
#- Set types: set, frozenset
#- Boolean: bool

#Example Follow-Up Tip: Explain the use of specific data types in your projects.


### 9. What is the difference between `@staticmethod`, `@classmethod`, and instance methods?
#Answer:
#- Instance method: Operates on an instance of the class.
#- Class method (`@classmethod`): Operates on the class itself, not on an instance.
#- Static method (`@staticmethod`): Does not operate on instance or class; behaves like a regular function within the class.

#Example:
class Example:
    def instance_method(self):
        return "Instance method called", self

    @classmethod
    def class_method(cls):
        return "Class method called", cls

    @staticmethod
    def static_method():
        return "Static method called"


### 10. What are Python’s comprehension techniques?
#Answer:
#Comprehensions provide a concise way to construct sequences.

#Example:
#- List Comprehension:
#squares = [x ** 2 for x in range(5)]  # [0, 1, 4, 9, 16]
#- **Dictionary Comprehension**:
#squares_dict = {x: x ** 2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
#- **Set Comprehension**:
#squares_set = {x ** 2 for x in range(5)}  # {0, 1, 4, 9, 16}


### **11. How would you handle exceptions in Python?**
#Answer:
#Use try-except blocks to catch and handle exceptions gracefully.

#Example:
try:
    x = int("not_a_number")
except ValueError as e:
    print(f"Error: {e}")
finally:
    print("This block always executes.")


### 12. Explain Python’s `with` statement.
#Answer:
#The with statement is used for resource management (e.g., file handling). It ensures that resources are properly released after use.

#Example:
#with open("file.txt", "r") as file:
#   content = file.read()


### 13. How does Python implement inheritance?
#Answer:
#Python supports single, multiple, and multilevel inheritance. Use the super() function to call parent class methods.

#Example:
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        super().greet()
        print("Hello from Child")

### 14. What are Python’s iterators and generators?
#Answer:
#- Iterators: Objects that implement __iter__() and __next__() methods.
#- Generators: Simplified way to create iterators using yield.

#Example:
def generator():
    for i in range(3):
        yield i

gen = generator()
print(next(gen))  # 0
print(next(gen))  # 1


### 15. What is the difference between `deepcopy()` and `copy()`?
#Answer:
#- `copy()`: Performs a shallow copy.
#- `deepcopy()`: Creates a deep copy.

#Example:
import copy
original = [[1, 2], [3, 4]]
deep = copy.deepcopy(original)


