import asyncio
import asyncpg

async def run():
    conn = await asyncpg.connect('postgresql://postgres:admin@localhost/postgres')

    print(conn)
    await conn.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(run())
