def get_user():
    return "Vivek"

# CLASS
class User:
    company = "OpenAI"

# CONSTRUCTOR
    def __init__(self, name):
        self.name = name

# ASSIGNED VALUE TO INSTANCE VARIABLE    
    def greet(self):
        print(f"Hello {self.name}")
        
# create object of class
user = User("Vivek")
user.greet()

u1 = User("Vivek")
u2 = User("John")

print(u1.company)
print(u2.company)

# inheritance
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    pass

dog = Dog()
dog.speak()

#method overriding
class Animal1:
    def speak(self):
        print("Animal sound")

class Dog1(Animal1):
    def speak(self):
        print("Bark")
        
dog1 = Dog1()
dog1.speak()

# super keyword of the c#
# -----------------------NEED TO READ AGAIN-----------------------
# class Animal2:
#     def __init__(self, name):
#         self.name = name

# class Dog2(Animal2):
#     def __init__(self, name):
#         super().__init__(name)
        
# dog2 = Dog2("Buddy")
# print(dog2.name)

# NOW REFERE email_service.py