#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Argparser.
"""

import argparse
import unittest

from unittest.mock import patch

def parse_cli_args():
    """Command line parser for subnet of interest.

    Args:
      IPv4 address.

    Returns:
      String, stripped of whitespace, e.g. 128.122.112.10
    """

    parser = argparse.ArgumentParser(description="IPv4 address of interest.")
    parser.add_argument("--ip", action="store", type=str,\
                        help="IP address of interest, e.g. 128.122.112.10")
    args = parser.parse_args()

    return args

class ParseCLITest(unittest.TestCase):

    """Unit tests.
    Use `patch()` to mock objects for testing.
    For reference: https://docs.python.org/3/library/unittest.mock.html
    """

    @patch('builtins.input', return_value='--ip 192.168.1.1')
    def test_parse_cli_args_01(self, input):
        """Valid return value.
        """
        self.assertEqual(parse_cli_args(), '192.168.1.1')

if __name__ == '__main__':
    args = parse_cli_args()
    unittest.main()
    #print(args.ip)
