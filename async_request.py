import aiohttp


async def ip_request():
    url = "http://jsonplaceholder.typicode.com/posts"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response_json = await response.json()
            return response_json[:10]
