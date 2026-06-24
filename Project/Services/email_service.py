# OLD APPROACH

# class User:
#     def __init__(self, id, name):
#         self.id = id
#         self.name = name
        
# NEW APPROACH
from dataclasses import dataclass

@dataclass
class User:
    id: int
    name: str
    
user = User(1, "Vivek")
print(user)

def calculate_tax(amount):
    return amount * 0.18