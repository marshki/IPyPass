#!/usr/bin/env python3
# pylint: disable=W0613,W0622

"""IPv4 validation using `ipaddress` module.

A ValueError is raised if address does not represent a valid IPv4.
For reference: https://docs.python.org/3/library/ipaddress.html
"""

import ipaddress
import unittest

from unittest.mock import patch

def ipv4_addr_check():
    """Prompt user for IPv4 address, then validate. Re-prompt if invalid."""

    while True:
        try:
            return ipaddress.IPv4Address(input('Enter valid IPv4 address: '))
        except ValueError:
            print('Bad value, try again.')
            raise

class IPv4AddrCheckTest(unittest.TestCase):
    """Unit tests.
    Use `patch()` to mock objects for testing.
    For reference: https://docs.python.org/3/library/unittest.mock.html
    """

    @patch('builtins.input', return_value='192.168.1.1')
    def test_ipv4_addr_check_01(self, input):
        """Valid return value."""
        self.assertIsInstance(ipv4_addr_check(), ipaddress.IPv4Address)

    @patch('builtins.input', return_value='10.0.0.1')
    def test_ipv4_addr_check_02(self, input):
        """Valid return value."""
        self.assertIsInstance(ipv4_addr_check(), ipaddress.IPv4Address)

    @patch('builtins.input', return_value='Derp!')
    def test_ipv4_addr_check_03(self, input):
        """Invalid return value."""
        with self.assertRaises(ValueError):
            ipv4_addr_check()

if __name__ == '__main__':
    unittest.main()
