import socket
import pickle

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

    def recve(self):
        data = self.socket.recv(1024)
        return pickle.loads(data)

    def close(self):
        self.socket.close()
