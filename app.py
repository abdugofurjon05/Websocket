import asyncio
from websockets.asyncio.server import serve


async def websocket_handler(websocket):
    websocket_id = str(websocket.id)[:6]

    
    print(f"Client connected: {websocket_id}")

    try:
        async for message in websocket: 
            await websocket.send(f"Echo: {message}")
    except Exception as e:
        print(f"Error with client {websocket_id}: {e}")
    finally:
        print(f"Client disconnected: {websocket_id}")



 
async def main():
    async with serve(websocket_handler, "localhost", 8765):
        print(f"WebSocket server started on ws://localhost:8765" )
        await asyncio.Future()  # Run forever


asyncio.run(main())


 
