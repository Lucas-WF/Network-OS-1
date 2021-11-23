import socket
import pickle
import threading

HOST = socket.gethostname()
PORT = 12345


class Server:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__listconn = []
        self.__datadict = {}

    def bind(self):
        self.socket.bind((HOST, PORT))

    def listen(self):
        self.socket.listen()

    def accept(self):
        conn, addr = self.socket.accept()
        self.__listconn.append(conn)
        self.__listconn.append(addr)

    def authorized_conn(self):
        conn, addr = self.__listconn
        print(f"Conexão estabelecida com: {addr[0]}, pela porta randomica: {addr[1]}")

    def recve(self, conn, addr):
        data = conn.recv(1024)
        data = pickle.loads(data)
        self.__datadict = {addr: data}

    def thread_recve(self):
        conn, addr = self.__listconn
        recv_thread = threading.Thread(target=self.recve, args=[conn, addr], daemon=True)
        recv_thread.start()

    @property
    def listconn(self):
        return self.__listconn

    @property
    def datadict(self):
        return self.__datadict

    def send(self, conn, data_s):
        data = data_s
        data = pickle.dumps(data)
        conn.sendall(data)

    def thread_send(self, data_t):
        conn, addr = self.__listconn
        send_thread = threading.Thread(target=self.send, args=[conn, data_t], daemon=True)
        send_thread.start()

    def close(self):
        self.socket.close()
        del self.__datadict
