# This is a simple Python script to print a greeting message
print("Hello Vivek")

# Activate the virtual environment before running the script:
# python -m venv venv
# venv\Scripts\activate

# how to freeze To freeze your Python environment and create a requirements file that lists all the installed packages, you can use the following command:
# pip install requests
# pip list
# pip freeze > requirements.txt
# pip install -r requirements.txt

# No type declaration needed for variables
name = "Vivek"      # str
age = 25            # int
salary = 10000.5    # float
is_active = True    # bool

# type checking of the variables
print(type(name))
print(type(age))
print(type(salary))
print(type(is_active))

# typecasting 
age = "25"
age_int = int(age)
print(type(age_int))

# string concatination
first = "Vivek"
last = "Parmar"

full = first + " " + last
print(full)

name = "Vivek"
print(f"Hello {name}")

# string methods
name = name.upper()
print(name)
name = name.lower()
print(name)
name = name.strip()
print(name)
name = name.replace("V", "J")
print(name)

# length check of string
print(len(name))

# List
# Creating Lists
# Indexing
# Negative Indexing
# Slicing
# append()
# insert()
# remove()
# pop()
# sort()
# Loop through Lists
# List Comprehension (important for interviews and AI development)
numbers = [10, 20, 30, 40, 50]

print(numbers[-2])
print(numbers[:3])
print(numbers[2:])
print(numbers[1:4])

# append() at last
names = ["Vivek", "John"]
names.append("Alice")
print(names)

#append at the choice index
names = ["Vivek", "John"]
names.insert(1, "Alice")
print(names)

#remove
names = ["Vivek", "John", "Alice"]
names.remove("John")
print(names)

#remove by index
names = ["Vivek", "John", "Alice"]
removed = names.pop(1)
print(removed)
print(names)

# sort the list
numbers = [5, 2, 8, 1]
numbers.sort()
print(numbers)

#sort the list in reverse order
numbers.sort(reverse=True)
print(numbers)

# predict below output of the following code snippet:

#syntax 1:
# names = ["Vivek", "John"]
# names.append("Alice")
# names.insert(1, "Bob")
# names.remove("John")
# print(names) 

#syntax 2:
# numbers = [5, 3, 8, 1]
# numbers.sort()
# print(numbers[-1])


# Lesson: Loops

# Loops are one of the most important concepts in Python.

# You'll use them in:
    # FastAPI APIs
    # Database records processing
    # File processing
    # JSON handling
    # AI workflows
    # RAG systems
    
names = ["Vivek", "John", "Alice"]

# normal for loop
for name in names:
    print(name)    

# range loop is used to generate a sequence of numbers. 
# It can be used in for loops to iterate over a specific range of numbers.    
for i in range(5):
    print(i)

print("Even numbers from 0 to 10:")
for i in range(0, 10, 2):
    print(i)
    
print("Number less than 5")
count = 1
while count <= 5:
    print(count)
    count += 1
    
# break

print("Break statement:")
for i in range(10):
    if i == 5:
        break

    print(i)
    
print("Continue statement:")

for i in range(5):
    if i == 2:
        continue
    print(i)
    
    
# tuples are similar to lists, but they are immutable, meaning their elements cannot be changed after creation. Tuples are defined using parentheses ().
names = ("Vivek", "John", "Alice")
print(names[0])

# lists are mutable, meaning their elements can be changed after creation. Lists are defined using square brackets [].
names = ["Vivek", "John"]
names.append("Alice")

# TUPLE USE IN BELOW CASES:
# db_config = (
#     "localhost",
#     5432,
#     "postgres"
# )

# sets

numbers = {1, 2, 3, 4}
print(numbers)

skills = {"Python", "SQL"}
skills.add("FastAPI")

print(skills)

skills.remove("SQL")
print(skills)

# dictonaries are used to store key-value pairs. They are defined using curly braces {}.
user = {
    "id": 1,
    "name": "Vivek",
    "city": "Ahmedabad"
}

for key, value in user.items():
    print(key, value)
    
print(user["name"])

user["email"] = "vivek@test.com"
print(user)

user["city"] = "Gandhinagar"

for key, value in user.items():
    print(key, value)
    
# Why Dictionaries Matter So Much
# Almost every API response is a dictionary.

# Conditional Statements

age = 25
if age >= 18:
    print("Adult")

print('------------------NEW--------------------')    
age = 16
if age >= 18:
    print("Adult")
else:
    print("Minor")
    
print('------------------NEW--------------------')
marks = 75

if marks >= 90:
    print("A")
elif marks >= 70:
    print("B")
elif marks >= 50:
    print("C")
else:
    print("Fail")
    
print('------------------NEW--------------------')
age = 25
salary = 100000

if age > 18 and salary > 50000:
    print("Eligible")
    
print('------------------NEW--------------------')
if age > 18 or salary > 50000:
    print("Eligible")
    
print('------------------NEW--------------------')
is_active = False

if not is_active:
    print("User Disabled")
    
print('------------------NEW--------------------')
result = "Adult" if age >= 18 else "Minor"
print(result)