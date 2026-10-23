# Handle how messages are sent and received over TCP

import struct
import json


def recv_exact(socket, n):
    data = b""

    while len(data) < n:
        received = socket.recv(n-len(data))

        if received == b"":
            raise ConnectionError("Connection with socket is closed.")

        data += received

    return data


def send_msg(socket, message):
    converted = json.dumps(message)
    payload = converted.encode("utf-8")

    length = len(payload)
    header = struct.pack("!I", length)

    socket.sendall(header + payload)


def receive_msg(socket):
    header = recv_exact(socket, 4)
    length = struct.unpack("!I", header)[0]
    payload = recv_exact(socket, length)

    decoded = payload.decode("utf-8")
    message = json.loads(decoded)

    return message
