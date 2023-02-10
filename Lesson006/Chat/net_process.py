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
                    data = conn.recv(1).decode('utf-8')
                    if data == 'r':
                        with open('messages.txt', 'r', encoding='utf-8') as f:
                            rec = f.read()
                        conn.send(rec.encode('utf-8'))
                    else:
                        message = ''
                        while True:
                                data = conn.recv(32)
                                if not data:
                                    break
                                message += data.decode('utf-8')
                                with open('messages.txt', 'a', encoding='utf-8') as f:
                                    f.write(message)

    def client_read_chat(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.server_address, 5000))
            s.send('r'.encode('utf-8'))
            rec = ''
            while True:
                data = s.recv(1024)
                if not data:
                    break
                rec += data.decode('utf-8')
        return rec

    def client_send_message(self, message: str):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.server_address, 5000))
            s.send(f'w{message}'.encode('utf-8'))
