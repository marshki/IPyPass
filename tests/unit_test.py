#!/usr/bin/env python3

"""Unit test class.
"""

import unittest
from ipaddress import IPv4Address
from io import StringIO
from contextlib import redirect_stdout
from ipypass.ipypass import parse_cli_args, eight_bit_passwd, twelve_bit_passwd, create_table

class IPyPassTests(unittest.TestCase):

    """Unit tests.
    """

    def test_parse_cli_args(self):
        """Test with and without valid IP address.
        """
        args = ['--ip', '192.168.0.1']
        ip = parse_cli_args(args)
        self.assertIsInstance(ip, IPv4Address)
        self.assertEqual(str(ip), '192.168.0.1')

        args = []
        ip = parse_cli_args(args)
        self.assertIsNone(ip)

    def test_eight_bit_passwd(self):
        """Test valid return value.
        """
        split_address = ['192', '168', '0', '1']
        password = eight_bit_passwd(split_address)
        self.assertEqual(password, '0*9*****')

    def test_twelve_bit_passwd(self):
        """Test valid return value.
        """
        split_address = ['192', '168', '0', '1']
        password = twelve_bit_passwd(split_address)
        self.assertEqual(password, '0*13*168****')

    def test_create_table(self):
        """Test talbe creation.
        """
        ip_address = IPv4Address('192.168.0.1')
        expected_output = '8-bit    12-bit     \n-------- ------------\n0*9***** 0*13*168****\n'
        with redirect_stdout(StringIO()) as output:
            create_table(ip_address)
            self.assertEqual(output.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
