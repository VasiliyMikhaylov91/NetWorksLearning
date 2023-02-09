# from socket import socket
# from threading import Thread
#
# chat_socket = socket()
# server_address = ('localhost', 1000)
# chat_socket.connect(server_address)
#
#
# def get_message():
#     while True:
#         print(chat_socket.recv(1024))
#
#
# def send_message():
#     while True:
#         chat_socket.sendall(input().encode(encoding='ascii'))
#
#
# Thread(target=get_message).start()
# Thread(target=send_message).start()

import socket
from json import dumps

# СоздаемTCP/IP сокет
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Подключаем сокет к порту, через который прослушивается сервер
server_address = ('localhost', 10000)
print('Подключено к {} порт {}'.format(*server_address))
sock.connect(server_address)

try:
    # Отправка данных
    messa = {"Mess": "Hello World!"}
    mess = dumps(messa)
    print(f'Отправка: {mess}')
    message = mess.encode()
    sock.sendall(message)

    # Смотрим ответ
    amount_received = 0
    amount_expected = len(message)
    while amount_received < amount_expected:
        data = sock.recv(32)
        amount_received += len(data)
        mess = data.decode()
        print(f'Получено: {data.decode()}')

finally:
    print('Закрываем сокет')
    sock.close()