#Should run the actual server
"""
- create TCP socket
- bind to 0.0.0.0:9090
- listen for clinets and accept connections
- use ThreadPoolExecutor and recieve requrests using protocol file
- determine what client wants and call appropriate storage function
- send response back with protocol file. (client sends Json style stuff)
"""

import protocol.py as prot
import socket

#create server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind()
server_socket.bind(("localhost", 5000))

#listen()
server_socket.listen()
print("Listening for a connection")

#accept()
client_socket, address = server_socket.accept()
print("Connection Established")
print("Address = " + address)

#handle clients
  
#call receive_msg()
  
#process requests
  
#call send_msg()
