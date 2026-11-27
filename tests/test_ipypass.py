#!/usr/bin/env python3

"""Unit test class."""

import unittest
from ipaddress import IPv4Address
from io import StringIO
from contextlib import redirect_stdout
from ipypass import parse_cli_args, eight_char_passwd, twelve_char_passwd, create_table

class IPyPassTests(unittest.TestCase):
    """Unit tests."""

    def test_parse_cli_args(self):
        """Test with and without valid IP address."""
        args = ['--ip', '192.168.0.1']
        ip_address = parse_cli_args(args)
        self.assertIsInstance(ip_address, IPv4Address)
        self.assertEqual(str(ip_address), '192.168.0.1')

        args = []
        ip_address = parse_cli_args(args)
        self.assertIsNone(ip_address)

    def test_eight_char_passwd(self):
        """Test valid return value."""
        split_address = ['192', '168', '0', '1']
        password = eight_char_passwd(split_address)
        self.assertEqual(password, '0*9*****')

    def test_twelve_char_passwd(self):
        """Test valid return value."""
        split_address = ['192', '168', '0', '1']
        password = twelve_char_passwd(split_address)
        self.assertEqual(password, '0*13*168****')

    def test_create_table(self):
        """Test table creation."""
        ip_address = IPv4Address('192.168.0.1')
        expected_output = '8-char   12-char    \n-------- ------------\n0*9***** 0*13*168****\n'
        with redirect_stdout(StringIO()) as output:
            create_table(ip_address)
            self.assertEqual(output.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
