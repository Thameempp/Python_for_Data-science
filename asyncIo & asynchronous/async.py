import asyncio

'''
-> async def → defines an asynchronous function (coroutine).
-> await asyncio.sleep(delay) → simulates a non-blocking delay (like an API call or I/O task).
-> asyncio.create_task() → schedules the coroutine to run concurrently.
-> asyncio.run(main()) → runs the event loop and executes the main coroutine.'''

async def main():
    task = asyncio.create_task(other_function()) #this task workds once there is a idle time
    print("A")
    await asyncio.sleep(1) # sleeps for  1 sec
    print("B")

# to get return value we need to await task (it doesn't effect its position , even if it is before print A )
    return_task = await task
    print(f"Return value: {return_task}")

async def other_function():
    print("1")
    await asyncio.sleep(2) # sleeps for  2 sec
    print("2")

# return value    
    return 10


asyncio.run(main())
