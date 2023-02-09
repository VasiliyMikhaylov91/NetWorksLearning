import socket


class network:
    def __init__(self, server: bool = True, server_address: str = ''):
        self.server_address = server_address
        self.server = server
        self.server_run = True

    def server_start(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.server_address, 5000))
            s.listen()
            while self.server_run:
                conn, addr = s.accept()
                with conn:
                    data = conn.recv(1)
                    if data == 'r':
                        with open('messages.txt', 'r', encoding='utf-8') as f:
                            conn.send(f.read())
                    else:
                        message = ''
                        while True:
                            data = conn.recv(32)
                            if not data:
                                break
                            message += data
                        with open('messages.txt', 'a', encoding='utf-8') as f:
                            f.write(message)

    def __client_init(self):
        pass
