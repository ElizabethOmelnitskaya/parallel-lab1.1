from settings import *
from asyncio import get_event_loop, Queue, start_server

processed, result, files = Queue(len(FILES)), 0, Queue()
loop = get_event_loop()
[files.put_nowait(f) for f in FILES]

async def process_a_new_connection (reader, writer):
    filename = await files.get()
    writer.write(filename.encode())

    await writer.drain()
    res = await reader.readuntil()
    writer.close()

    global result
    result += int(res.decode().rstrip())

    await processed.put(filename)
    if processed.full():
        print(f'word <<{WORD}>> appeared {result} times')
        loop.stop()

coro = start_server(process_a_new_connection, ADDR, PORT, loop=loop)
server = loop.run_until_complete(coro)

try:
    loop.run_forever()
finally:
    server.close()
