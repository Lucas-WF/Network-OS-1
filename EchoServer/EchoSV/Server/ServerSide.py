import socket
import pickle
from EchoSV.controller.IMC_Calc import IMC

HOST = socket.gethostname()
PORT = 12345


class Server:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__listconn = []  # Cria uma lista para guardar os valores de conn e addr

    def bind(self):
        self.socket.bind((HOST, PORT))  # Associa o socket ao local host com a porta X

    def listen(self, client: type(object)):  # Escuta as tentativas de conexão de entrada
        self.socket.listen()
        client.connect()  # E faz uma associação com a Classe cliente

    def accept(self):
        conn, addr = self.socket.accept()
        self.__listconn.append(conn)
        self.__listconn.append(addr)

        # Aceita a primeira conexão e cria um novo socket (conn) e devolve o endereço da conexão (addr)

    def authorized_conn(self):
        conn, addr = self.__listconn
        print(f"Conexão estabelecida com: {addr[0]}, pela porta randomica: {addr[1]}")  # Imprime o endereço da conexão

    def recve(self):
        conn, addr = self.__listconn
        data = conn.recv(1024)
        data = pickle.loads(data)
        w, h, a = data[0], data[1], data[2]
        imc = IMC(weight=w, height=h, age=a)
        data = imc.calc()
        data = pickle.dumps(data)
        conn.sendall(data)  # Transmite os dados para client

    def close(self):  # Termina a conexão
        conn, addr = self.__listconn
        conn.close()
        self.socket.close()
        del self.__listconn


if __name__ == "__main__":
    print("Classe Server")
