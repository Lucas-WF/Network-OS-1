import socket
import pickle
import threading
import time

HOST = socket.gethostname()
PORT = 12345


class Client:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.socket.connect((HOST, PORT))

    def send(self, data_i):
        data = pickle.dumps(data_i)
        self.socket.sendall(data)

    def send_thread(self, data_t):
        thread = threading.Thread(target=self.send, args=[data_t], daemon=True)
        thread.start()

    def recve(self):
        data = self.socket.recv(1024)
        return pickle.loads(data)

    def close(self):
        self.socket.close()
