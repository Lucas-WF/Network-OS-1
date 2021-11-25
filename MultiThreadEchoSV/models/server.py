import socket
import pickle

HOST = socket.gethostname()
PORT = 12345


class Server:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def create_listen_socket(self):
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((HOST, PORT))
        self.socket.listen()

    def accept(self):
        conn, addr = self.socket.accept()
        print(f"Conexão estabelecida com: {addr[0]}, pela porta randomica: {addr[1]}")
        return conn, addr

    def recve(self, conn, addr):
        data = conn.recv(1024)
        data = pickle.loads(data)
        return data

    def send(self, data_s, conn):
        data = data_s
        data = pickle.dumps(data)
        conn.sendall(data)

    def close(self):
        self.socket.close()
