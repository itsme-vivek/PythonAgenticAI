# sequential call
# import asyncio

# async def task1():
#     print("Task 1 Started")
#     await asyncio.sleep(2)
#     print("Task 1 Finished")

# async def task2():
#     print("Task 2 Started")
#     await asyncio.sleep(2)
#     print("Task 2 Finished")

# async def main():
#     await task1()
#     await task2()

# asyncio.run(main())

import asyncio

async def task1():
    print("Task 1 Started")
    await asyncio.sleep(2)
    print("Task 1 Finished")

async def task2():
    print("Task 2 Started")
    await asyncio.sleep(2)
    print("Task 2 Finished")

async def main():
    await asyncio.gather(
        task1(),
        task2()
    )

asyncio.run(main())

print('------------SECOND EXAMPLE------------')
import asyncio

async def square(number):
    await asyncio.sleep(1)
    return number * number

async def main():

    results = await asyncio.gather(
        square(2),
        square(3),
        square(4)
    )

    print(results)

asyncio.run(main()) #gather() returns results in the same order as the coroutines you passed in.

# Use gather() when:
    # Making multiple API calls.
    # Running independent database queries.
    # Reading multiple files.
    # Calling several AI tools.
    
    
# c#
# await Task.WhenAll(
#     task1,
#     task2,
#     task3
# );