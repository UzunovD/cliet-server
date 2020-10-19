import logging
import os
import sys

LOG = logging.getLogger('msngr.client')

PATH = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(PATH, 'logs', 'client.log')

HANDLER_FILE = logging.FileHandler(PATH, encoding='utf-8')
HANDLER_FILE.setLevel(logging.DEBUG)
HANDLER_STREAM = logging.StreamHandler(sys.stderr)
HANDLER_STREAM.setLevel(logging.ERROR)

FORMATTER = logging.Formatter("%(asctime)-30s %(levelname)-10s "
                              "%(module)-20s %(message)s")
HANDLER_FILE.setFormatter(FORMATTER)
HANDLER_STREAM.setFormatter(FORMATTER)

LOG.addHandler(HANDLER_FILE)
LOG.addHandler(HANDLER_STREAM)
LOG.setLevel(logging.INFO)

if __name__ == '__main__':
    LOG.info('Test logging')
    LOG.error('Test logging')
