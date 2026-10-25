import asyncio

from .services.clients import doer

if __name__ == "__main__":
    asyncio.run(doer())
