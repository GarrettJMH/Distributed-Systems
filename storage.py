# Store data and make access thread-safe.
import threading

storage = {}

queue = []

condition = threading.Condition()

lock = threading.Lock()


def put(key, value):
    with lock:
        storage[key] = value


def get(key):
    with lock:
        return storage.get(key)


def enqueue(value):
    with condition:
        queue.append(value)
        condition.notify()


def dequeue():
    with condition:
        while len(queue) == 0:
            condition.wait()

        return queue.pop(0)
