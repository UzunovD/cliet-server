"""Unittests for server.py."""
import unittest

from common.varyb import (ACCOUNT_NAME, ACTION, ERROR, PRESENCE, RESPONSE,
                          TIME, TYPE, USER)
from server import process_clnt_msg


class TestServer(unittest.TestCase):
    """class for testing server.py."""

    def testprocessclntmsg(self):
        """Test for server.process_clnt_msg() with correct message."""
        message = {
            ACTION: PRESENCE,
            TIME: 1.1,
            TYPE: 'service info',
            USER: {
                ACCOUNT_NAME: 'Guest',
            },
        }
        self.assertEqual(process_clnt_msg(message), {RESPONSE: 200})

    def testprocessclntmsgtype(self):
        """Test for server.process_clnt_msg() for type return."""
        message = {
            ACTION: PRESENCE,
            TIME: 1.1,
            TYPE: 'service info',
            USER: {
                ACCOUNT_NAME: 'Guest',
            },
        }
        self.assertEqual(type(process_clnt_msg(message)), type({}))

    def testprocessclntmsg400(self):
        """Test for server.process_clnt_msg() with incorrect message."""
        message = {
            ACTION: PRESENCE,
            TIME: 1.1,
            USER: {
                ACCOUNT_NAME: 'Guest',
            },
        }
        mess = message.copy()
        for _ in message:
            key, value = mess.popitem()
            self.assertEqual(
                process_clnt_msg(mess),
                {RESPONSE: 400,
                 ERROR: 'Bad Request',
                 })
            mess[key] = value

    def testprocessclntmsg400monty(self):
        """Test for server.process_clnt_msg() with incorrect account name."""
        message = {
            ACTION: PRESENCE,
            TIME: 1.1,
            USER: {
                ACCOUNT_NAME: 'Monty',
            },
        }
        self.assertEqual(
            process_clnt_msg(message),
            {RESPONSE: 400,
             ERROR: 'Bad Request',
             })


if __name__ == '__main__':
    unittest.main()
