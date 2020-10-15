"""Server program."""

import argparse
import ipaddress
import json
import socket
import sys

from common.utils import get_message, send_message
from common.varyb import (ACCOUNT_NAME, ACTION, ERROR, MAX_CONNECTIONS,
                          PRESENCE, RESPONSE, TIME, USER)


def process_clnt_msg(message):
    """
    Обработчик сообщений от клиентов.

    принимает словарь -
    сообщение от клинта, проверяет корректность,
    возвращает словарь-ответ для клиента

    :param message: :dict
    :return: dict
    """
    if ACTION in message and message[ACTION] == PRESENCE and TIME in message \
            and USER in message and message[USER][ACCOUNT_NAME] == 'Guest':
        return {RESPONSE: 200}
    return {
        RESPONSE: 400,
        ERROR: 'Bad Request',
    }


def main():
    """
    Загрузка параметров командной строки, если нет параметров, то задаём значения по умоланию.

    Сначала обрабатываем адрес, потом порт:
    server.py -a 192.168.1.2 -p 8079
    :return:
    """

    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-a',
        '--addr_ip',
        type=str,
        help='IP addr for connect, default=0.0.0.0',
        default='0.0.0.0')
    parser.add_argument(
        '-p',
        '--port',
        type=int,
        help='Port for connect, default=8888',
        default=8888)

    args = parser.parse_args()
    try:
        listen_port = args.port
        if 1024 > listen_port > 65535:
            raise ValueError
    except ValueError:
        print(
            'В качастве порта может быть указано только число в диапазоне от 1024 до 65535.')
        sys.exit(1)

    # Затем загружаем какой адрес слушать

    if args.addr_ip != 'localhost':
        try:
            ipaddress.ip_address(args.addr_ip)
        except ValueError:
            print(
                'После параметра \'a\'- необходимо указать адрес, который будет слушать сервер.')
            sys.exit(1)
    listen_address = args.addr_ip

    # Готовим сокет

    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    transport.bind((listen_address, listen_port))

    # Слушаем порт

    transport.listen(MAX_CONNECTIONS)

    while True:
        client, client_address = transport.accept()
        try:
            msg_from_clnt = get_message(client)
            response = process_clnt_msg(msg_from_clnt)
            send_message(client, response)
            client.close()
        except (ValueError, json.JSONDecodeError):
            print('Принято некорретное сообщение от клиента.')
            client.close()


if __name__ == '__main__':
    main()
