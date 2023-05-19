import asyncio
import websockets


async def handle_connection(websocket, path):
    while True:
        try:
            message = await websocket.recv()
            if message == 'exit':
                print("Connection closed")
                exit(0)
            print(f"Received message: {message}")

            response = "Server received"
            await websocket.send(response)
            print(f"Sent response: {response}")
        except Exception as e:
            print(str(e))

start_server = websockets.serve(handle_connection, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
