import logging
import os
import sys
from logging.handlers import TimedRotatingFileHandler

LOG = logging.getLogger('msngr.server')

PATH = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(PATH, 'logs', 'server.log')

HANDLER_FALE = TimedRotatingFileHandler(
    PATH, when='H',
    interval=1,
    encoding='utf-8',
)
HANDLER_FALE.setLevel(logging.DEBUG)
HANDLER_STREAM = logging.StreamHandler(sys.stderr)
HANDLER_STREAM.setLevel(logging.ERROR)

FORMATTER = logging.Formatter("%(asctime)-30s %(levelname)-10s "
                              "%(module)-20s %(message)s")
HANDLER_FALE.setFormatter(FORMATTER)
HANDLER_STREAM.setFormatter(FORMATTER)

LOG.addHandler(HANDLER_FALE)
LOG.addHandler(HANDLER_STREAM)
LOG.setLevel(logging.DEBUG)

if __name__ == '__main__':
    LOG.info('Test logging')
    LOG.error('Test logging')
