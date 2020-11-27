# import asyncio
import asyncpg


async def write_db(posts):
    conn = await asyncpg.connect(
        'postgresql://postgres:admin@localhost/postgres'
        # 'postgresql://postgres:admin@localhost:32768/dvdrental'
        # user='postgres',
        # password='admin',
        # database='dvdrental',
        # host='localhost'
    )
    # rows = await conn.fetch("SELECT * FROM actor;")
    # print(type(rows))
    # for row in rows[:15]:
    #     print(row)
    # row = await conn.fetchrow(
    #     'SELECT * FROM actor WHERE first_name = $1', "John")
    # print(row)

    # await conn.execute('''
    #         CREATE TABLE posts(
    #             id serial PRIMARY KEY,
    #             title text,
    #             body text
    #         )
    #     ''')
    # for post in posts:
    #     await conn.execute(
    #         "INSERT INTO posts(id, title, body) VALUES($1, $2, $3)",
    #         post['id'],
    #         post['title'],
    #         post['body'],
    #     )

    await conn.close()

#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(run())
