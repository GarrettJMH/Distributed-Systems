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
import concurrent.futures

def handler(client_socket):

    try:
      while True:
        request = prot.receive_msg(client_socket)
        print(f"Received: {request}")

        message = {
          "test": "message"
        }
        
        prot.send_msg(client_socket, message)

    except ConnectionError:
      print("Connection Error")
      
    finally:
      client_socket.close()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(("0.0.0.0", 9090))

server_socket.listen()
print("Listening for a connection")

with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
  while True:
    client_socket, address = server_socket.accept()
    print("Connection Established")
    print(f"Address = {address}")

    executor.submit(handler, client_socket)
  
