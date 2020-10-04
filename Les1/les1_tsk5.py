# 5.	Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из
# байтовового в строковый тип на кириллице.
import subprocess
import chardet


def ping(target: str):
    '''
    Ping target and print result

    :param target: IP or symbol name web source
    :return: str
    '''
    args = ['ping', target]
    subp_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
    for line in subp_ping.stdout:
        codec = chardet.detect(line).get('encoding')
        print(line.decode(codec))


sites = ['yandex.ru', 'youtube.com']
for site in sites:
    ping(site)
