"""Client program"""
import argparse
import ipaddress
import json
import socket
import sys
import time

from common.utils import get_message, send_message
from common.varyb import (ACCOUNT_NAME, ACTION, ERROR, PRESENCE, RESPONSE,
                          TIME, TYPE, USER)


def create_presence(account_name='Guest'):
    '''
    Функция генерирует запрос о присутствии клиента
    :param account_name:
    :return:
    '''
    out = {
        ACTION: PRESENCE,
        TIME: time.time(),
        TYPE: 'service info',
        USER: {
            ACCOUNT_NAME: account_name,
        },
    }
    return out


def proc_answ(message):
    '''
    Функция разбирает ответ сервера
    :param message:
    :return:
    '''
    if RESPONSE in message:
        if message[RESPONSE] == 200:
            return '200 : OK'
        return f'400 : {message[ERROR]}'
    raise ValueError


def main():
    '''Загружаем параметы коммандной строки'''

    parser = argparse.ArgumentParser()

    parser.add_argument('-a', '--addr_ip', type=str, help='IP addr for connect, default=localhost', default='127.0.0.1')
    parser.add_argument('-p', '--port', type=int, help='Port for connect, default=8888', default=8888)

    args = parser.parse_args()
    try:
        server_port = args.port
        if server_port < 1024 or server_port > 65535:
            raise ValueError
    except ValueError:
        print('В качестве порта может быть указано только число в диапазоне от 1024 до 65535.')
        sys.exit(1)

    try:
        ipaddress.ip_address(args.addr_ip)
    except ValueError:
        print(
            'После параметра \'a\'- необходимо указать адрес, который будет слушать сервер.')
        sys.exit(1)
    else:
        server_address = args.addr_ip

    # Инициализация сокета и обмен

    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    transport.connect((server_address, server_port))
    message_to_server = create_presence()
    send_message(transport, message_to_server)
    try:
        answer = proc_answ(get_message(transport))
        print(answer)
    except (ValueError, json.JSONDecodeError):
        print('Не удалось декодировать сообщение сервера.')


if __name__ == '__main__':
    main()
