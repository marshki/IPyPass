#!/usr/bin/env python3

"""IPv4 validation using `ipaddress module` and argparse."""

import argparse
from ipaddress import ip_address

import unittest
from unittest.mock import patch

def parse_cli_args():
    """
    Command line parser for subnet of interest.

    Args:
      --ip 0.0.0.0

    Returns:
      String, e.g. 0.0.0.0

    """

    parser = argparse.ArgumentParser(description="IPv4 address of interest.")
    parser.add_argument("--ip", action="store", type=ip_address,\
                        required=True,\
                        help="IP address of interest, e.g. 0.0.0.0")

    args = parser.parse_args()

    return args

class ParseCLIArgsTest(unittest.TestCase):

    """

    Unit tests.
    """

    #def setUp(self):
    #    self.parser = parser_cli_args()

    @patch('builtins.input', return_value='192.168.1.1')
    def test_parse_cli_args(self, input):
        """Valid return value."""
        args = parse_cli_args(['--ip ', '192.168.1.1'])
        self.assertIsInstance(parser_cli_args(), '192.168.1.1')

if __name__ == '__main__':
    #args = parse_cli_args()
    #print(args.ip)
    unittest.main()
