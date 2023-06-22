#!/usr/bin/env python3

"""IPv4 validation using `ipaddress module` and argparse."""

import argparse
import ipaddress
import unittest

from ipaddress import IPv4Address
from unittest.mock import patch

def parse_cli_args():
    """
    Command line parser for IPv4 address of interest, with validation.

    Returns:
        IPv4 address as an instance of ipaddress.IPv4Address, or None if no IP address is provided.

    Raises:
        argparse.ArgumentTypeError: If the IP address is invalid.
    """

    parser = argparse.ArgumentParser(description="IPv4 address of interest.")
    parser.add_argument("--ip", action="store", type=ipaddress.IPv4Address,
                        required=False,
                        help="IP address of interest, e.g. 0.0.0.0")
    args = parser.parse_args()

    return args.ip

class IPyPassTests(unittest.TestCase):
    """Unit tests."""

    @patch('sys.argv', ['script_name', '--ip', '192.168.0.1'])
    def test_parse_cli_args(self):
        ip = parse_cli_args()
        self.assertIsInstance(ip, IPv4Address)
        self.assertEqual(str(ip), '192.168.0.1')

    @patch('sys.argv', ['script_name'])
    def test_parse_cli_args_no_ip(self):
        ip = parse_cli_args()
        self.assertIsNone(ip)

if __name__ == '__main__':
    unittest.main()
