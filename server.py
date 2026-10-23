#Should run the actual server

import protocol as prot
import socket
import concurrent.futures
import storage as s

def process_request(request):
    action = request.get("action")

    if action == "GET":
        s.get(request)

    elif action == "PUT":
        s.put(request)
        

    elif action == "ENQUEUE":
        s.enqueue(request)
        

    elif action == "DEQUEUE":
        s.dequeue(request)
        

    else:
        return {
            "status": "ERROR",
            "message": "Action not found"
        }
    

def handler(client_socket):

    try:
      while True:
        request = prot.receive_msg(client_socket)
        print(f"Received: {request}")

        response = process_request(request)
        
        prot.send_msg(client_socket, response)

    except ConnectionError:
      print("Connection Error")
      
    finally:
      client_socket.close()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(("0.0.0.0", 9090))

server_socket.listen()
print("Listening for a connection")

with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
  while True:
    client_socket, address = server_socket.accept()
    print("Connection Established")
    print(f"Address = {address}")

    executor.submit(handler, client_socket)
  
