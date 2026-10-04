#Handle how messages are sent and received over TCP
"""
This file should:
- turn a Python dictionary into JSON
- encode JSON into bytes
- put the 4-byte length header in front
- send the full message
- receive exactly 4 bytes for the header
- determine how long the message is
- receive exactly that many bytes
- turn the bytes back into JSON/Python data
"""

import struct
import json

def recv_exact(socket, n):
  data = b""

  while len(data) < n:
    recieved = socket.recv(n-len(data))
    data += recieved

    if revieved = b"":
      raise ConnectionError("Connection with socket is closed.")

  return data


def send_msg(socket, message):
  
  converted = json.dumps(message)

  payload = converted.encode("utf-8")

  length = len(payload)

  header = struct.pack("!I", length)

  socket.sendall(header + payload)

def receive_msg(socket):

  header = recv_exact(socket, 4)

  length = struct.unpack("!I", header)

  payload = recv_exact(socket, length)

  decoded = payload.decode("utf-8")

  message = json.loads(decoded)

  return message
