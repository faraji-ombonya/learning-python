import asyncio

HOST = '0.0.0.0'
PORT = 50007

async def handle_client(reader, writer):
    addr = writer.get_extra_info('peername')
    print('Connected by', addr)

    while True:
        data = await reader.read(100)  # Read up to 100 bytes
        if not data:
            break
        writer.write(data)  # Echo back the data
        await writer.drain()  # Ensure the data is sent

    print('Disconnected by', addr)
    writer.close()

async def main():
    server = await asyncio.start_server(handle_client, HOST, PORT)
    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')

    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())
