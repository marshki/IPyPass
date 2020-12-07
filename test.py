#!/usr/bin/env python3

import argparse
import unittest

from ipaddress import ip_address
from unittest.mock import patch

def parse_cli_args():
    """
    Command line parser for subnet of interest.

    Args:
      IPv4 address.

    Returns:
      String, e.g. 0.0.0.0

    """

    parser = argparse.ArgumentParser(description="IPv4 address of interest.")
    parser.add_argument("--ip", action="store", type=ip_address,\
                        required=True,\
                        help="IP address of interest, e.g. 0.0.0.0")
    args = parser.parse_args()

    return args

class ParserTest(unittest.TestCase):
    def setUp(self):
        self.parser = parser_cli_args()

    def test_IP(self):
        parser = self.parser.parse_args(['--ip ', '192.168.1.1'])
        self.assertEqual(parser_cli_args(), '192.168.1.1')

if __name__ == '__main__':
    #args = parse_cli_args()
    #print(args.ip)
    unittest.main()
