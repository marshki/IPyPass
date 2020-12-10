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

if __name__ == '__main__':
    args = parse_cli_args()
    print(args.ip)
