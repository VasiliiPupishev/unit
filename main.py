import asyncio
import websockets
import threading
from Mail import Mailer

lock = threading.RLock()
mailer = Mailer()


def write_in_file(message):
    base_file = open('README.txt', 'a')
    base_file.write(message + "\n")


async def mark(websocket, path):
    async for message in websocket:
        with lock:
            write_in_file(message)
            mailer.send_mail(message)


def main():
    start_server = websockets.serve(mark, "localhost", 8080)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()


if __name__ == "__main__":
    main()
