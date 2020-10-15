"""Unit tests for client.py."""
import unittest

from client import create_presence, proc_answ
from common.varyb import (ACCOUNT_NAME, ACTION, ERROR, PRESENCE, RESPONSE,
                          TIME, TYPE, USER)


class TestClient(unittest.TestCase):
    """class for tests for client.py."""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testcreatepresencedef(self):
        """Test for correct request with default account name."""
        request = create_presence()
        request[TIME] = 1.1
        self.assertEqual(request, {
            ACTION: PRESENCE,
            TIME: 1.1,
            TYPE: 'service info',
            USER: {
                ACCOUNT_NAME: 'Guest',
            },
        })

    def testcreatepresence(self):
        """Test for correct request with custom account name."""
        request = create_presence('Monty')
        request[TIME] = 1.1
        self.assertEqual(request, {
            ACTION: PRESENCE,
            TIME: 1.1,
            TYPE: 'service info',
            USER: {
                ACCOUNT_NAME: 'Monty',
            },
        })

    def testparseanswer200(self):
        """Test for correct answer 200."""
        response = proc_answ({RESPONSE: 200})
        self.assertEqual(response, '200 : OK')

    def testparseanswer400(self):
        """Test for correct answer 400."""
        answ = proc_answ({RESPONSE: 201, ERROR: 'Bad Request'})
        self.assertEqual(answ, '400 : Bad Request')

    def testparseanswererr(self):
        """Test for incorrect answer."""
        with self.assertRaises(ValueError):
            proc_answ({})


if __name__ == '__main__':
    unittest.main()
