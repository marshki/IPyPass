#!/usr/bin/env python3

import argparse

def parse_cli_args():
    """Command line parser for subnet of interest.

    Args:
      IPv4 address.

    Returns:
      String, e.g. 0.0.0.0

    """

    parser = argparse.ArgumentParser(description="IPv4 address of interest.")
    parser.add_argument("--ip", action="store", type=str,\
                        help="IP address of interest, e.g. 0.0.0.0")
    args = parser.parse_args()

    if args.ip is None:
        parser.error("--ip requires an IPv4 adddress. None specified.")

    return args

if __name__ == '__main__':
    args = parse_cli_args()
    print(args.ip)
