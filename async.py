import asyncio
import time

async def say_after2(say, sleep):
    print("say after2 function is running")
    await asyncio.sleep(sleep)
    print(say)
    await asyncio.sleep(sleep)
    print(say)

async def say_after(say, sleep):
    print("say after function is running")
    await asyncio.sleep(sleep)
    print(say)
    await say_after2("hello world", 1)

    await asyncio.sleep(sleep)
    print(say)

    
async def main():
    # task1 = asyncio.create_task(
    #     say_after("first task", 3)
    # )
    # task2 = asyncio.create_task(
    #     say_after("second task", 1)
    # )
    print(f"started at {time.strftime('%X')}")
    print("start running tasks")

    await say_after("hello", 1)
    print("start running task1")
    await say_after("world", 1)
    print(f"ended at {time.strftime('%X')}")

asyncio.run(main())