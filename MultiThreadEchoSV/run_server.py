from models.server import Server
from models.imc import Imc
import threading

server = Server()
datadict = {}


def create_server():
    server.create_listen_socket()


def accept():
    return server.accept()


def handle_server_recv(connect, address):
    while True:
        try:
            data = server.recve(conn=connect, addr=address)
            if data == "close":
                server.close()
            datadict[address] = data
        except EOFError:
            print(f"Cliente: {addr[0]} | {addr[1]}, desconectado.")
            break

def handle_server_send(connect, address):
    while True:
        for i in list(datadict):
            if i == address:
                value = datadict[i]
                imc = Imc(*value)
                server.send(imc.calc(), connect)
                datadict.pop(i)


if __name__ == "__main__":
    create_server()
    while True:
        conn, addr = accept()
        recv_thread = threading.Thread(target=handle_server_recv, args=[conn, addr], daemon=True)
        send_thread = threading.Thread(target=handle_server_send, args=[conn, addr], daemon=True)
        recv_thread.start()
        send_thread.start()
