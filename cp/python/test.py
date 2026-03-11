import asyncio

async def set_future_result(future, value) :
    await asyncio.sleep(2)
    # Set the result of the future
    future.set_result(value)
    print(f"Set the future's result to: {value}")

async def main():
    # Create a future object
    loop = asyncio.get_running_loop()
    future = loop. create_future()

    # Schedule setting the future's result
    asyncio. create_task(set_future_result(future, "Future result is ready"))

    # Wait for the future's result
    result = await future
    print(f"Received the future's result: {result}")



'''
async def fetch_data(id, sleep_time):
    print(f"Coroutine {id} starting to fetch data.")
    await asyncio.sleep(sleep_time)
    return {"id": id, "data": f"Sample data from coroutine {id}"}

async def main():
    # Create tasks for running coroutines concurrently
    tasks = []
    async with asyncio.TaskGroup() as tg:
        for i,sleep_time in enumerate([2,3,1],start=1):
            task = tg.create_task(fetch_data(i,sleep_time))
            tasks.append(task)
    for res in tasks:
        print(f"Recived result : {res.result()}")
'''
asyncio. run(main())