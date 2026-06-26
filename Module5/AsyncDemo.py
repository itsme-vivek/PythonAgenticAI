# By the end of this lesson, you'll understand:
    # What synchronous code is
    # What asynchronous code is
    # When to use async
    # When not to use async
    # Why FastAPI uses async
    # Why AI applications use async

# Important: Today we're learning the concept. In the next lesson, we'll write actual asyncio code.


# Synchronouse Programming
# def make_tea():
#     print("Making tea")

# def make_coffee():
#     print("Making coffee")

# make_tea()
# make_coffee()

# e.g2
# import time

# print("Start")

# time.sleep(5)

# print("Finished")


# Concept - Synchronous Programming

# Take Order
# ↓
# Go to Kitchen
# ↓
# Stand there...
# ↓
# Bring Food
# ↓
# Next Customer
# The waiter wastes time waiting.

# Concept - ASynchronous Programming

# Take Order (Table 1)
# ↓
# Kitchen starts cooking
# ↓
# Take Order (Table 2)
# ↓
# Kitchen starts cooking
# ↓
# Take Order (Table 3)
# ↓
# Serve whichever meal is ready
# The waiter stays productive

def greet1():
    print("Hello")

result = greet1()

print(result)

async def greet():
    print("Hello")

result2 = greet()

print(result2)

import asyncio

asyncio.run(greet())

# example 3
import asyncio

print('------TEST-----')
async def greet3():
    print("Start")
    await asyncio.sleep(3)
    print("End")

async def greet4():
    print("Start")
    print("End")
    
asyncio.run(greet3())
asyncio.run(greet4())

print('-----------Async Myth-----------------')

import asyncio

async def task1():
    print("Task 1")
    await asyncio.sleep(2)

async def task2():
    print("Task 2")
    await asyncio.sleep(2)

async def main():
    await task1()
    await task2()

asyncio.run(main()) #waits until task1() completes before starting task2().

# asyncio.create_task()
# asyncio.gather()