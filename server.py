import asyncio
import websockets

async def server(websocket, path):
    print(f"Conexão estabelecida com {path}")

    try:
        while True:
            message = await websocket.recv()
            print(f"Mensagem recebida do usuário: {message}")

            response = input("IFRN: ")
            await websocket.send(response)
    except websockets.exceptions.ConnectionClosedError:
        print(f"Conexão encerrada com {path}")

start_server = websockets.serve(server, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
