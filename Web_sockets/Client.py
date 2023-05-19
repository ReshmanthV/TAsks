import asyncio
import websockets


async def send_message():
    async with websockets.connect("ws://localhost:8765") as websocket:
        while True:
            try:
                message = input("Enter a message('exit' for close): ")
                await websocket.send(message)
                if message == 'exit':
                    print("Connection Closed")
                    exit(0)
                print(f"Sent message: {message}")

                response = await websocket.recv()
                print(f"Received response: {response}")
            except Exception as e:
                print(str(e))


asyncio.get_event_loop().run_until_complete(send_message())
