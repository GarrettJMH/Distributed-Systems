# Test server with clients

import socket
import protocol as prot
import concurrent.futures

HOST = "localhost"
PORT = 9090
NUM_CLIENTS = 20


def run_client(clientid):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((HOST, PORT))

        key = f"key{clientid}"
        value = f"value{clientid}"
        task = f"task{clientid}"

        # PUT
        prot.send_msg(client_socket, {
            "action": "PUT",
            "key": key,
            "value": value
        })

        put_response = prot.receive_msg(client_socket)

        if put_response.get("status") != "OK":
            return False, None

        # GET
        prot.send_msg(client_socket, {
            "action": "GET",
            "key": key
        })

        get_response = prot.receive_msg(client_socket)

        if get_response.get("value") != value:
            return False, None

        # ENQUEUE
        prot.send_msg(client_socket, {
            "action": "ENQUEUE",
            "value": task
        })

        enqueue_response = prot.receive_msg(client_socket)

        if enqueue_response.get("status") != "OK":
            return False, None

        # DEQUEUE
        prot.send_msg(client_socket, {
            "action": "DEQUEUE"
        })

        dequeue_response = prot.receive_msg(client_socket)

        dequeued_value = dequeue_response.get("value")

        print(f"Client {clientid}: PASS")

        return True, dequeued_value

    except Exception as e:
        print(f"Client {clientid}: ERROR - {e}")
        return False, None

    finally:
        client_socket.close()


results = []

print(f"Launching {NUM_CLIENTS} concurrent client workers...")

with concurrent.futures.ThreadPoolExecutor(max_workers=NUM_CLIENTS) as executor:

    futures = [
        executor.submit(run_client, client_id)
        for client_id in range(NUM_CLIENTS)
    ]

    for future in futures:
        results.append(future.result())

client_results = [
    result[0]
    for result in results
]

dequeued_values = [
    result[1]
    for result in results
]

expected_tasks = {
    f"task{i}"
    for i in range(NUM_CLIENTS)
}


if (
    set(dequeued_values) == expected_tasks
    and len(dequeued_values) == NUM_CLIENTS
):
    print("Queue verification: PASS")
else:
    print("Queue verification: FAIL")

if all(client_results):
    print("Client verification: PASS")
else:
    print("Client verification: FAIL")

print(f"All {NUM_CLIENTS} client workers completed.")
