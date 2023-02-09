import socket


class network:
    def __init__(self, server: bool = True, server_address: str = ''):
        self.server_address = server_address
        self.server = server
        if server:
            self.__server_init()
        else:
            self.__client_init()

    def __server_init(self):
        pass

    def __client_init(self):
        pass