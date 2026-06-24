# Module2
# Functions
# ↓
# Modules & Imports
# ↓
# Exception Handling
# ↓
# OOP

# Normal Function
def greet():
    print("Hello Vivek")
    
greet()

# Parameterized Function
def greetParameter(name):
    print(f"Hello, {name}. How are you doing?")
    
greetParameter("Vivek")

# returning Function
def add(a, b):
    return a + b

result = add(5, 3)
print(result)

# Hint: You can also specify the data type of the parameters and return type in Python using type hints. 
# This is optional but can help with code readability and debugging.
def addHint(a: int, b: int) -> int:
    return a + b

result = addHint(4,5)
print(result)

# multiple returns - It will return a tuple
def get_user():
    return 1, "Vivek"

user_id, name = get_user()

print(user_id)
print(name)

# default parameters
def greet1(name="Guest"):
    print(f"Hello {name}")
    
greet1()
greet1("Vivek")

def create_user(name, age):
    print(name, age)
    
create_user(age=25, name="Vivek")

print('------------------NEW-------------------- Output will be in tuple format --------------------')
print('args will Accepts multiple positional arguments.')
def add(*numbers):
    print(numbers)
    
add(1, 2, 3, 4, 5)

print('real life example of *args')
def total(*numbers):
    return sum(numbers)

print(total(10, 20))
print(total(10, 20, 30))

print('----**kwargs-------')
print('Accepts dynamic named arguments.Need to use when we need output like dictionary format.')
# kwargs is a dictionary.

def user_info(**kwargs):
    print(kwargs)
    
user_info(
    name="Vivek",
    city="Ahmedabad"
)

def user_info1(**kwargs):
    print(kwargs["name"])

user_info1(
    name="Vivek",
    city="Ahmedabad"
)


# lambda functions vs normal functions

# normal function
def square(x):
    return x * x

# lambda functions
square1 = lambda x: x * x

print(square(3))
print(square1(5))


# mostly lambda are using for the sorting
employees = [
    {"name": "John", "salary": 50000},
    {"name": "Vivek", "salary": 100000},
    {"name": "Alice", "salary": 75000}
]

employees.sort(
    key=lambda emp: emp["salary"]
)

print(employees)

# function + dictonaries
def get_user():
    return {
        "id": 1,
        "name": "Vivek",
        "city": "Ahmedabad"
    }

user = get_user()

print(user["name"])

# Next Topic: Modules & Imports

