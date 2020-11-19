#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Argparser.
"""

import argparse

def parse_cli_args():
    """Command line parser for subnet of interest.

    Args:
      IPv4 address.

    Returns:
      String, stripped of whitespace, e.g. 128.122.112.10
    """

    parser = argparse.ArgumentParser(description="IPv4 address of interest.")
    parser.add_argument("--IP", help="IP address of interest, e.g. 128.122.112.10 ")
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = parse_cli_args()
    print(args.IP)
