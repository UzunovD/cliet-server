"""Client program."""
import argparse
import ipaddress
import json
import logging
import socket
import sys
import time

from common.utils import get_message, send_message
from common.varyb import (ACCOUNT_NAME, ACTION, ERROR, PRESENCE, RESPONSE,
                          TIME, TYPE, USER)
from log import client_log_config

LOG = logging.getLogger('msngr.client')


def create_presence(account_name='Guest'):
    """
    Функция генерирует запрос о присутствии клиента.

    :param account_name: str
    :return: Возвращает словарь - сообщение о присутствии
    """
    out = {
        ACTION: PRESENCE,
        TIME: time.time(),
        TYPE: 'service info',
        USER: {
            ACCOUNT_NAME: account_name,
        },
    }
    return out


def proc_answ(message: dict):
    """
    Функция разбирает ответ сервера.

    :param message:
    :return:
    """
    if RESPONSE in message:
        if message.get(RESPONSE, None) == 200:
            LOG.info(f'Server answered {message}, client will send "code 200"')
            return '200 : OK'
        LOG.warning(f'Server answered {message}, client will send "code 400"')
        return f'400 : {message[ERROR]}'
    LOG.error(f"Can't parse server's answer {message}")
    raise ValueError


def main():
    """Загружаем параметы коммандной строки."""
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-a',
        '--addr_ip',
        type=str,
        help='IP addr for connect, default=localhost',
        default='127.0.0.1')
    parser.add_argument(
        '-p',
        '--port',
        type=int,
        help='Port for connect, default=8888', default=8888)

    args = parser.parse_args()
    try:
        server_port = args.port
        if server_port < 1024 or server_port > 65535:
            raise ValueError
    except ValueError:
        LOG.error(
            f'{ValueError} В качестве порта может быть указано только '
            f'число в диапазоне от 1024 до 65535.'
        )
        sys.exit(1)

    else:
        try:
            ipaddress.ip_address(args.addr_ip)
        except ValueError:
            LOG.error(
                f'{ValueError} После параметра \'a\'- необходимо указать '
                f'адрес, который будет слушать сервер.'
            )
            sys.exit(1)
        else:
            server_address = args.addr_ip
            LOG.info('Клиент запущен с параметрами: адрес и порт сервера '
                     f'{server_address}, {server_port}')

    # Инициализация сокета и обмен

    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        transport.connect((server_address, server_port))
        message_to_server = create_presence()
        send_message(transport, message_to_server)
    except Exception as e:
        LOG.error(repr(e))
        sys.exit(1)
    else:
        try:
            answer = proc_answ(get_message(transport))
            LOG.info(f'Answer from server: {answer}')
        except (ValueError, json.JSONDecodeError):
            LOG.error(
                f'{ValueError} Не удалось декодировать сообщение сервера.'
            )


if __name__ == '__main__':
    main()
