import os.path
from tkinter import *

from threading import Thread
from net_process import network


class chat:
    def __init__(self):
        self.server = None
        self.user_name = None
        self.ip_address = None
        self.messages = []
        self.send_btn = None
        self.message = None
        self.chat_box = None
        self.chat_frame = None
        self.root = None
        self.message_frame = None
        self.__autorisating()

    def __update_chat(self):
        if self.server:
            if not os.path.exists('messages.txt'):
                with open('messages.txt', 'w', encoding='utf-8') as file:
                    file.writelines(self.messages)
            if self.server:
                with open('messages.txt', 'r', encoding='utf-8') as file:
                    self.messages = file.readlines()
        else:
            nw = network(self.server, self.ip_address)
            self.messages = nw.client_read_chat().split('\n')
        value = Variable(value=self.messages)
        self.chat_box.config(listvariable=value)
        self.chat_box.after(500, self.__update_chat)

    def __send_message(self, event):
        if self.server:
            text = self.message.get()
            if text:
                with open('messages.txt', 'a', encoding='utf-8') as file:
                    file.write(f'{self.user_name}: {text}\n')
        else:
            nw = network(self.server, self.ip_address)
            nw.client_send_message(f'{self.user_name}: {self.message.get()}\n')
        self.message.delete(0, 'end')

    def main_window(self):
        self.root = Tk()
        self.root.title(f'{self.user_name} chat')
        self.root.geometry('500x560')
        self.root.resizable(False, False)
        self.chat_frame = Frame(self.root, height=30, width=80)
        self.chat_box = Listbox(master=self.chat_frame, height=30, width=80)
        self.chat_box.after(500, self.__update_chat)
        self.chat_box.pack()
        self.chat_frame.pack(padx=10)
        self.message_frame = Frame(master=self.root, height=4, width=80)
        Label(master=self.message_frame, text='Введите сообщение:').grid(row=0, column=0)
        self.message = Entry(master=self.message_frame, width=50)
        self.message.bind('<Return>', self.__send_message)
        self.message.grid(row=1, column=0)
        self.send_btn = Button(master=self.message_frame, text='Отправить', width=20, padx=2, pady=2)
        self.send_btn.bind('<ButtonPress-1>', self.__send_message)
        self.send_btn.grid(row=1, column=1, padx=10)
        self.message_frame.pack()
        if self.user_name:
            self.root.mainloop()
        if self.server:
            os.remove('./messages.txt')
            self.nw.server_run = False

    def __server_process(self):
        self.nw = network(self.server)
        self.nw.server_start()

    def __start_chat(self, svr):
        self.user_name = self.name_entry.get()
        self.server = svr.get()
        self.ip_address = self.ip_address_entry.get()
        self.inwindow.destroy()
        if self.server:
            self.serv_thread = Thread(target=self.__server_process)
            self.serv_thread.start()

    def __autorisating(self):
        self.inwindow = Tk()
        self.inwindow.title('Авторизация')
        self.inwindow.geometry('250x250')
        Label(master=self.inwindow, text='Введите никнейм:').pack(anchor='nw', padx=5)
        self.name_entry = Entry(master=self.inwindow, width=20)
        self.name_entry.pack(anchor='nw', padx=5)
        server = IntVar()
        self.server_checkbutton = Checkbutton(text='Стать сервером', variable=server)
        self.server_checkbutton.pack(anchor='nw')
        self.ip_address_entry = Entry(master=self.inwindow, width=20)
        self.ip_address_entry.pack(anchor='nw', padx=5)
        self.start_chat_button = Button(text='Начать чат', command=lambda: self.__start_chat(server))
        self.start_chat_button.pack(anchor='center')
        self.inwindow.mainloop()


if __name__ == "__main__":
    chat_1 = chat()
    if chat_1.user_name:
        chat_1.main_window()
