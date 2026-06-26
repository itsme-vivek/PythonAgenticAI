def calculate_total( prices: list[float]) -> float:
    total_cost : float = 0.0
    for price in prices:
        total_cost = total_cost + float(price)
    return total_cost

print(calculate_total([10.0,10.0]))

from typing import TypedDict

class Employee(TypedDict):
    id: int
    name: str
    salary: float
    
employee : Employee = {
    'id':1,
    'name':"Vivek",
    'salary':20.0
}

employees: list[Employee] = [
    {
        "id": 1,
        "name": "Vivek",
        "salary": 20000.0
    },
    {
        "id": 2,
        "name": "John",
        "salary": 30000.0
    },
    {
        "id": 3,
        "name": "Alice",
        "salary": 40000.0
    }
]

for employee in employees:
    print(employee["name"])
    print(employee["salary"])