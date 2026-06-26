# without hints

# def add(a, b):
#     return a + b

# with type hints

# def add(a: int, b: int) -> int:
#     return a + b

# Define the data type as following method for the varible
name: str = 'Vivek'

age: int = 10

salary: float = 10.2

is_active: bool = True

names: list[str] = [
    "Vivek",
    "John"
]

user: dict[str, str] = {
    "name": "Vivek",
    "city": "Ahmedabad"
}

scores: dict[str, float]


location: tuple[float, float]
location = (
    23.0225,
    72.5714
)

def get_email() -> str | None:
    return None


from typing import Any
data: Any

# Type Aliases

# Instead of repeating same follow below approach
dict[str, list[str]]
type UserRoles = dict[str, list[str]]
roles: UserRoles

# TypedDict 

# Python doesn't know the expected structure.
user = {
    "name": "Vivek",
    "age": "25"
}

# updated version that we should follow
from typing import TypedDict

class User1(TypedDict):
    name: str
    age: int
    
user1: User1 = {
    "name": "Vivek",
    "age": 25
}

# Benifits:
#     Your IDE can now:
#         autocomplete keys,
#         warn about missing keys,
#         catch incorrect value types.


# Normal API response processing method

# {
#     "id": 1,
#     "title": "iPhone",
#     "price": 999
# }

# product = response.json()

# Newer and best approach
from typing import TypedDict

class Product(TypedDict):
    id: int
    title: str
    price: float
    
# product: Product = response.json()


# type hints in the classes

class User2:

    def __init__(
        self,
        name: str,
        age: int
    ):

        self.name: str = name
        self.age: int = age
        

# type hints with collections
usersDic: list[dict[str, str]]

users = [
    {
        "name": "Vivek",
        "city": "Ahmedabad"
    },
    {
        "name": "John",
        "city": "London"
    }
]


# why we should go for the type hints

# FastAPI automatically:

# validates the type,
# generates OpenAPI documentation,
# generates Swagger UI,
# returns a 422 response if the type is invalid.

# This is one of the biggest reasons FastAPI became so popular

# Use type hints for:
    # Function parameters
    # Return values
    # Class attributes
    # Public APIs
    
