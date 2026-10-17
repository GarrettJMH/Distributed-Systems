#Store data and make access thread-safe. Should contain key-value store and queue
import threading

storage = {}

queue = []

lock = threading.Lock()

def put(key, value):
  with lock:
    

def get(key):


def enqueue(value):


def dequeue():

