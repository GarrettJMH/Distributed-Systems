#Should run the actual server
"""
- create TCP socket
- bind to 0.0.0.0:9090
- listen for clinets and accept connections
- use ThreadPoolExecutor and recieve requrests using protocol file
- determine what client wants and call appropriate storage function
- send response back with protocol file. (client sends Json style stuff)
"""

import protocol as prot
import socket

def handler(client_socket):

  while True:
    try:
      request = prot.recieve_msg(client_socket)
      print(f"Recieved: {request}")
    
      prot.send_msg(client_socket, message)

    except ConnectionError:
      print("Connection Error")
      break
      
    client_socket.close()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(("0.0.0.0", 9090))

message = {
    "test": "message"
  }

server_socket.listen()
      print("Listening for a connection")
      
      address = server_socket.accept()
      print("Connection Established")
      print(f"Address = {address}")
