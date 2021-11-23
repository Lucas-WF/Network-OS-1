import tkinter
from tkinter import *
from tkinter import messagebox


class Application(tkinter.Tk):

    def __init__(self, controller):
        self.controller = controller
        super().__init__()
        self.font = ("Copperplate Gothic Bold", "14", "italic", "bold")
        self.font_value4 = ("Copperplate Gothic Bold", "11", "italic", "bold")
        self.button_font = ("Rockwell Extra Bold", "12", "bold")
        self.iconbitmap(r"C:\Users\User\PycharmProjects\MultiThreadEchoSV\view\images\favicon.ico")
        self.title("ICM")
        self.geometry("650x450+400+100")
        self.resizable(width=False, height=False)
        self.protocol("WM_DELETE_WINDOW", self.closeapp)

        self.background_image = PhotoImage(file=r"""C:\Users\User\PycharmProjects\MultiThreadEchoSV\view\images\wp4118594.png""")
        self.background_image = self.background_image.subsample(1, 1)
        self.background_label = Label(self, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.image = PhotoImage(file=r"C:\Users\User\PycharmProjects\MultiThreadEchoSV\view\images\logo.png")
        self.image = self.image.subsample(4, 4)
        self.logo = Label(self.background_label, image=self.image, relief=SUNKEN)
        self.logo.pack(pady=15)

        self.top_container = Frame(self.background_label, pady=10, bg="#0E1A40", borderwidth=3, relief=RAISED)
        self.top_container.pack(side=TOP, fill=None, expand=False)

        self.center_container = Frame(self.background_label, pady=10, bg="#0E1A40", borderwidth=3, relief=RAISED)
        self.center_container.pack(fill=None, expand=False)

        self.left_center_container = Frame(self.center_container, padx=10, bg="#0E1A40")
        self.left_center_container.pack(side=LEFT, fill=BOTH, expand=False)

        self.right_center_container = Frame(self.center_container, padx=10, bg="#0E1A40")
        self.right_center_container.pack(side=RIGHT, fill=BOTH, expand=False)

        self.under_center_container = Frame(self.background_label, bg="#0E1A40", borderwidth=3, relief=RAISED, pady=10)
        self.under_center_container.pack(fill=None, expand=False)

        self.left_under_center_container = Frame(self.under_center_container, padx=10, bg="#0E1A40")
        self.left_under_center_container.pack(side=LEFT, fill=BOTH, expand=False)

        self.right_under_center_container = Frame(self.under_center_container, padx=10, bg="#0E1A40")
        self.right_under_center_container.pack(side=RIGHT, fill=BOTH, expand=False)

        self.upper_bottom_container = Frame(self.background_label, pady=10, bg="#0E1A40", borderwidth=3, relief=RAISED)
        self.upper_bottom_container.pack(fill=None, expand=False)

        self.left_upper_bottom_container = Frame(self.upper_bottom_container, padx=10, bg="#0E1A40")
        self.left_upper_bottom_container.pack(side=LEFT, fill=BOTH, expand=False)

        self.right_upper_bottom_container = Frame(self.upper_bottom_container, padx=10, bg="#0E1A40")
        self.right_upper_bottom_container.pack(side=RIGHT, fill=BOTH, expand=False)

        self.bottom_container = Frame(self.background_label, pady=10, bg="#0E1A40", borderwidth=3, relief=RAISED)
        self.bottom_container.pack(side=BOTTOM, fill=None, expand=False)

        self.left_bottom_container = Frame(self.bottom_container, padx=32.5, bg="#0E1A40")
        self.left_bottom_container.pack(side=LEFT, fill=BOTH, expand=False)

        self.right_bottom_container = Frame(self.bottom_container, padx=20, bg="#0E1A40")
        self.right_bottom_container.pack(side=RIGHT, fill=BOTH, expand=False)

        self.title = Label(self.top_container, text="CALCULADORA DO IMC", fg="#8131A2", bg="#0E1A40")
        self.title.config(font=self.font)
        self.title.pack(side=TOP)

        self.value1 = Label(self.left_center_container, text="Peso", width=10, borderwidth=2, relief="raised",
                            fg="#8131A2")
        self.value1.config(font=self.font)
        self.value1.pack(side=LEFT)

        self.entryvar1 = StringVar()
        self.entryvar2 = StringVar()
        self.entryvar3 = StringVar()

        self.entry1 = Entry(self.right_center_container, width=10, borderwidth=2, relief="solid", fg="#8131A2",
                            textvariable=self.entryvar1)
        self.entry1.config(font=self.font)
        self.entry1.pack(side=RIGHT)

        self.value2 = Label(self.left_under_center_container, text="Altura", width=10, borderwidth=2, relief="raised",
                            fg="#8131A2")
        self.value2.config(font=self.font)
        self.value2.pack(side=LEFT)

        self.entry2 = Entry(self.right_under_center_container, width=10, borderwidth=2, relief="solid", fg="#8131A2",
                            textvariable=self.entryvar2)
        self.entry2.config(font=self.font)
        self.entry2.pack(side=RIGHT)

        self.value3 = Label(self.left_upper_bottom_container, text="Idade", width=10, borderwidth=2, relief="raised",
                            fg="#8131A2")
        self.value3.config(font=self.font)
        self.value3.pack(side=LEFT)

        self.entry3 = Entry(self.right_upper_bottom_container, width=10, borderwidth=2, relief="solid", fg="#8131A2",
                            textvariable=self.entryvar3)
        self.entry3.config(font=self.font)
        self.entry3.pack(side=RIGHT)

        self.value4 = Label(self.right_bottom_container, text="", width=40, borderwidth=2, relief="raised",
                            fg="#8131A2", pady=5)
        self.value4.config(font=self.font_value4)
        self.value4.pack()

        self.calculate_button = Button(self.left_bottom_container, text="Calcular",
                                       command=self.response, font=self.button_font, fg="#8131A2")
        self.calculate_button.pack()

    def get_entry(self):
        self.entryvar1.set("1"), self.entryvar2.set("1"), self.entryvar3.set("1")
        return self.entryvar1.get(), self.entryvar2.get(), self.entryvar3.get()

    def response(self):
        data = self.controller.send_msg()
        self.value4["text"] = data

    def main_v(self):
        self.mainloop()

    def closeapp(self):
        if messagebox.askyesno("Sair", "Você tem certeza que deseja sair?"):
            self.destroy()
            exit()
