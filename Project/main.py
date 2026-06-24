from Services.user_service import get_user
import utils.math_utils as mu

user = get_user()
print(user)

print(mu.add(10, 20))


# Exception handling
# try
# except
# finally
# raise
# custom exceptions

# run this code direct
# x1 = 10 / 0
# print(x1)
    
# run with try except
try:
    x = 10 / 0
    print(x)
except:
    print("Error")
    
    
# catch specific exception
try:
    num = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
    
# handle multiple exceptions
try:
    number = int("abc")
except ValueError:
    print("Invalid number")
except ZeroDivisionError:
    print("Division by zero")

# use exception object    
try:
    number = int("abc")
except Exception as ex:
    print(ex)
    
# raise exception
# age = 15

# if age < 18:
#     raise Exception("Age must be 18 or above")

# EXAMPLE
print()
def get_user(user_id):
    if user_id <= 0:
        raise ValueError("Invalid user id")

    return {"id": user_id}

try:
    user = get_user(-1)
except ValueError as ex:
    print(ex)
    
# Exception
# ├── ValueError
# ├── TypeError
# ├── KeyError
# ├── IndexError
# ├── ZeroDivisionError
# ├── FileNotFoundError
# └── ImportError

# OOPS

class User:
    pass

user = User()


# NOW REFER USERSERVICE