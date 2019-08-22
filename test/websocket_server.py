#!/usr/bin/env python

import asyncio
import websockets

async def hello(websocket, path):
    print("In hello")
    message = await websocket.recv()
    print(f"< {message}")

    reply = f"Received {message}!"

    await websocket.send(reply)
    print(f"> {reply}")

start_server = websockets.serve(hello, 'localhost', 8765)
print("Started server")
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()