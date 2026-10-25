import asyncio
from ..limiter import gateway


async def hitter(client_name:str,hits:int,delay:int):
    results = []
    for _ in range(hits):
        response = gateway.handle_request(client_name)
        results.append(response)
        await asyncio.sleep(delay)
    return results
    
async def doer():
    requests = {
        "A": {10:1},
        "B": {20:0.6},
        "C": {5:1}
    }
    print(f"Starting concurrent Simulation for client {list(requests.keys())}")
    results = await asyncio.gather(
                        *list(
                            hitter(client_name,hits,delay) 
                            for client_name,definer in requests.items() 
                            for hits,delay in definer.items()))
    print("All tasks finished")
    print(f"Result list: {results}")


if __name__ == "__main__":
    asyncio.run(doer())
