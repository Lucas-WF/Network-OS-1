from view.tkinter_app import Application
from models import server, imc, client


class Controller:

    def __init__(self):
        self.view = Application(self)
        self.server = server.Server()
        self.client = client.Client()
        self.server.bind()
        self.server.listen()
        self.client.connect()
        self.server.accept()
        self.server.authorized_conn()

    def dict_search(self):
        for i, x in self.server.datadict.items():
            if i == self.server.listconn[1]:
                peso, idade, altura = x
                return peso, idade, altura

    def send_msg(self):
        self.client.send_thread(self.view.get_entry())
        self.server.thread_recve()
        self.model = imc.IMC(*self.dict_search())
        result = self.model.calc()
        self.server.thread_send(result)
        return self.client.recve()

    def run(self):
        self.view.main_v()
