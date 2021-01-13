#!/usr/bin/env python3

"""IPv4 validation using `ipaddress module` and argparse."""

import argparse

import unittest

def parse_cli_args():
    """
    Command line parser for subnet of interest.
    Args:
      --ip 0.0.0.0
    Returns:
         String, e.g. 0.0.0.0
    """

    parser = argparse.ArgumentParser(description="IPv4 address of interest.")
    parser.add_argument("--ip", action="store", type=str,\
                        required=True,\
                        help="IP address of interest, e.g. 0.0.0.0")

    return parser

class ParseCLIArgs(unittest.TestCase):

    """
    Unit tests.
    """
    def setUp(self):
        self.parser = parse_cli_args()

    def test_parser_cli_args_01(self):
        """Valid return value."""
        parsed = self.parser.parse_args(['--ip', '192.168.1.1'])
        self.assertEqual(parsed.ip, '192.168.1.1')

    def test_parser_cli_args_02(self):
        """Valid return value."""
        parsed = self.parser.parse_args(['--ip', '10.0.0.1'])
        self.assertEqual(parsed.ip, '10.0.0.1')

if __name__ == '__main__':
    unittest.main()
