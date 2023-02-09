import socket
from GUI import chat


class network:
    def __init__(self, GUI: chat):
        self.server_address = GUI.ip_address
        self.server = GUI.server

    def server_start(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.server_address, 5000))
            s.listen()
            while True:
                conn, addr = s.accept()
                with conn:
                    data = conn.recv(1)
                    if data == 'r':
                        pass

    def __client_init(self):
        pass
