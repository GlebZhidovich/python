import asyncio
from async_request import ip_request

async def main():
    data = await ip_request()
    print(data)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
