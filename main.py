import asyncio
from async_request import ip_request
from conect_db import write_db


async def main():
    posts = await ip_request()
    await write_db(posts)
    # for post in posts:
    #     print(post['id'])
    #     print(post['title'])
    #     print(post['body'])


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
