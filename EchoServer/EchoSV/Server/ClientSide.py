import socket
import pickle

HOST = socket.gethostname()  # Local Host
PORT = 12345  # Porta aleatória


class Client:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Cria o socket

    def connect(self):
        self.socket.connect((HOST, PORT))  # Conecta ao Host na porta X

    def send(self, v1, v2, v3):
        data = pickle.dumps((v1, v2, v3))
        self.socket.sendall(data)

    def recve(self):
        data = self.socket.recv(1024)  # Recebe os dados do server
        return pickle.loads(data)

    def close(self):
        self.socket.close()  # termina a conexão


if __name__ == "__main__":
    print("Class Client")
