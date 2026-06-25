import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/users/1"
)

print(response)
print(response.status_code)
print(response.text)
print(response.json())

response_data = response.json()
print(response_data["name"])

if response.status_code == 200:
    data = response.json()
    print(data["email"])
else:
    print("Request failed")
    
# NEW API Request With Query Param
# https://example.com/users?page=1&limit=10
params = {
    "page": 1,
    "limit": 10
}

response1 = requests.get(
    "https://example.com/users",
    params=params
)

print(response1.text)

#New API Request With the Header
# headers = {
#     "Authorization": "Bearer YOUR_TOKEN",
#     "Accept": "application/json"
# }

# response = requests.get(
#     url,
#     headers=headers
# )

# Send a Post Request
import requests

payload = {
    "name": "Vivek",
    "city": "Ahmedabad"
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/users",
    json=payload #this line will convert dictonary to JSON it will set as Content-Type: application/json
)

print(response.status_code)
print(response.json())

# production ready API Call

# url = ''
# response = requests.get(url)

# import requests

# try:
#     response = requests.get(url, timeout=10)
#     response.raise_for_status()

#     data = response.json()

# except requests.exceptions.RequestException as ex:
#     print(ex)
    
    
# New Ex to just how we can handle the many type of exception for generic messages
# import requests

# try:
#     response = requests.get(url, timeout=5)
#     response.raise_for_status()

# except requests.exceptions.Timeout:
#     print("Request timed out")

# except requests.exceptions.ConnectionError:
#     print("Cannot connect")

# except requests.exceptions.HTTPError as ex:
#     print(ex)

# except requests.exceptions.RequestException as ex:
#     print(ex)
    
# Session - Suppose you're making many API requests to the same server
# MISTAKE
# requests.get(...)
# requests.get(...)
# requests.get(...)

# CORECTION - USE SESSION
# BENIFITS
# Reuses TCP connections.
# Improves performance.
# Stores cookies automatically.
# import requests

# session = requests.Session()

# response1 = session.get(url1)
# response2 = session.get(url2)
# response3 = session.get(url3)

# SAMPLE
# import requests

# headers = {
#     "Authorization": "Bearer YOUR_API_KEY"
# }

# payload = {
#     "model": "gpt-4",
#     "messages": [
#         {
#             "role": "user",
#             "content": "Hello"
#         }
#     ]
# }

# response = requests.post(
#     url,
#     headers=headers,
#     json=payload,
#     timeout=30
# )

# NEW SAMPLE API 
import requests

def get_user(user_id):
    url = f"https://api.example.com/users/{user_id}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as ex:
        print(ex)
        return None
print('--------------Test---------------')    
get_user(1)

# | .NET (`HttpClient`)     | Python (`requests`) |
# | ----------------------- | ------------------- |
# | `GetAsync()`            | `requests.get()`    |
# | `PostAsync()`           | `requests.post()`   |
# | `ReadAsStringAsync()`   | `response.text`     |
# | JSON deserialization    | `response.json()`   |
# | Default request headers | `headers={...}`     |
# | Timeout                 | `timeout=10`        |


# Python Naming Convention
# C# > Python
# GetUser() > get_user()
# UserService > UserService
# BaseUrl > base_url

#Modules & Packages
# A module is simply a Python file (.py) that contains reusable code.
# c# static class is best example 

# python eg

# math_utils.py

# def add(a, b):
#     return a + b

# Different way to import the module
# Import Entire Module
# Import Specific Function
# Import Multiple Function
# Alias


# Python Built In Modules

import math
print(math.sqrt(25))

import random
print(random.randint(1, 10))

import random
print(random.randint(1, 10))

import os
print(os.getcwd())

# Package
# A package is a folder containing Python modules.

# project/

# services/
#     user_service.py
#     email_service.py

# utils/
#     math_utils.py

# main.py

# Structure E.g
# hotel_app/

# api/
#     booking_api.py
#     payment_api.py

# services/
#     booking_service.py
#     payment_service.py

# models/
#     booking.py
#     hotel.py

# config/
#     settings.py

# utils/
#     logger.py

# main.py

# What is __init__.py?
# __init__.py(Package initialization)
# __init__() (Class constructor)
# statement 1

# services/
# user_service.py
# hotel_service.py

# statement 2 - with this Now Python treats services as a package

# services/
# __init__.py

# e.g of init
# START

# user_service.py

print("1")
# def get_user():
#     return "Vivek"

# __init__.py
print("2")
# from .user_service import get_user

# main.py
print("3")
# from services import get_user
# print(get_user())


# Use it mainly for:

# exports
# package metadata
# very lightweight initialization
#end


# statment 3 purpopse of __name__
# Think of it as "only run this block when the file is executed directly."

# math_utils.py
print(__name__)

# environment variable
# pip install python-dotenv

# from dotenv import load_dotenv
# import os

# load_dotenv()

# api_key = os.getenv("API_KEY")

# print(api_key)

timeout = os.getenv("TIMEOUT", "30")