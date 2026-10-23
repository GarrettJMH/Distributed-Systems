#Test server
"""
- create multiple client connections to :9090
- send different protocol requests and run many at the same time
- make sure responses are correct and detect problems
"""

import socket
import protocol as prot

HOST = "localhost"
PORT = 9090

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))

print("Connected.")

request = {
  "action": "PUT",
  "key": "namme",
  "value": "Garrett"
}

prot.send_msg(client, request)

response = prot.receive_msg(client)

print("PUT response:", response)

request = {
    "action": "GET",
    "key": "name"
}

prot.send_msg(client_socket, request)

response = prot.receive_msg(client_socket)

print("GET response:", response)

request = {
    "action": "ENQUEUE",
    "value": "task1"
}

prot.send_msg(client_socket, request)

response = prot.receive_msg(client_socket)

print("ENQUEUE response:", response)

request = {
    "action": "DEQUEUE"
}

prot.send_msg(client_socket, request)

response = prot.receive_msg(client_socket)

print("DEQUEUE response:", response)


client_socket.close()
