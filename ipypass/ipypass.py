#!/usr/bin/env python3

"""Take IPv4 addresss and return 8-bit, 12-bit passwords."""

import ipaddress
import argparse

def parse_cli_args():
    """
    Command line parser for IPv4 address of interest.

    Args: IPv4 address, e.g.: --ip 0.0.0.0
    Returns: String, e.g.: 0.0.0.0

    """

    parser = argparse.ArgumentParser(description="IPv4 address of interest.")
    parser.add_argument("--ip", action="store", type=str,\
                        help="IP address of interest, e.g. 0.0.0.0")
    args = parser.parse_args()

    return args

def ipv4_addr_check():
    """
    Validate IPv4 address.

    Args: IPv4 address, e.g.: 0.0.0.0
    Returns: String-converted IPv4 address, e.g.: 0.0.0.0
    Raises: ValueError.

    """
    while True:
        try:
            return str(ipaddress.IPv4Address(input('Enter valid IPv4 address: ')))
        except ValueError:
            print('Bad value, try again.')

def eight_bit_passwd():
    """
    Transform IP address to 8-bit password.

    Args: String-converted IPv4 address, split by octet.
    Returns: 8-bit password.

    """
    return((SPLIT_ADDRESS[2] + '*' +
            str(int(SPLIT_ADDRESS[3]) + 8)).ljust(8, '*'))

def twelve_bit_passwd():
    """
    Transform IP address to 12-bit password.

    Args: String-converted IPv4 address, split by octet.
    Returns: 12-bit password.

    """
    return((SPLIT_ADDRESS[2] + '*' +
            str(int(SPLIT_ADDRESS[3]) + 12) + '*' + SPLIT_ADDRESS[1]).ljust(12, '*'))

def create_table():
    """
    Create a crude table.

    Returns: Table with transformed output.

    """

    print('8-bit   ', '12-bit     ')
    print('--------', '------------')
    print(eight_bit_passwd(), twelve_bit_passwd())

if __name__ == '__main__':
    args = parse_cli_args()

    if args.ip:
        ADDRESS = args.ip
        SPLIT_ADDRESS = ADDRESS.split('.', 4)
        create_table()
    else:
        ADDRESS = ipv4_addr_check()
        SPLIT_ADDRESS = ADDRESS.split('.', 4)
        create_table()
