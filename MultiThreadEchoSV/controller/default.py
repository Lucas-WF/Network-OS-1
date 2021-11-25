from view.tkinter_app import Application
from models.client import Client


class Controller:
    def __init__(self):
        self.view = Application(self)
        self.client = Client()
        self.client.connect()

    def run(self):
        self.view.main_v()

    def control_send(self):
        self.client.send(self.view.get_entry())

    def control_recv(self):
        return self.client.recve()

    def close(self):
        self.client.close()
