#!/usr/bin/env python3

"""Take IPv4 addresss and return 8- or 12-bit password (CLI).
"""

import ipaddress
import argparse

def ipv4_addr_check():
    """Validate IPv4 address.

    Args:
      IPv4 address of the form: 0.0.0.0
    
    Returns: 
      String-converted IPv4 address.

    Raises: 
      ValueError.
    """

    while True:
        try:
            return str(ipaddress.IPv4Address(input('Enter valid IPv4 address: ')))
        except ValueError:
            print('Bad value, try again.')

def parse_cli_args():
    """Command line parser for subnet of interest.

    Args:
      IPv4 address of the form: 0.0.0.0

    Returns:
      String, stripped of whitespace, e.g. 128.122.112.10
    """

    parser = argparse.ArgumentParser(description="IPv4 address of interest.")
    parser.add_argument("--ip", help="IP address of interest, e.g. 128.122.112.10 ")
    args = parser.parse_args()
    return args

def eight_bit_passwd():
    """Transform IP address to 8-bit password.
    Args: String-converted IPv4 address, split by octet.
    Returns: 8-bit password.
    """
    return((SPLIT_ADDRESS[2] + '*' +
            str(int(SPLIT_ADDRESS[3]) + 8)).ljust(8, '*'))

def twelve_bit_passwd():
    """Transform IP address to 12-bit password.
    Args: String-converted IPv4 address, split by octet.
    Returns: 12-bit password.
    """
    return((SPLIT_ADDRESS[2] + '*' +
            str(int(SPLIT_ADDRESS[3]) + 12) + '*' + SPLIT_ADDRESS[1]).ljust(12, '*'))

if __name__ == '__main__':
    ADDRESS = ipv4_addr_check()
    SPLIT_ADDRESS = ADDRESS.split('.', 4)
    print('8-bit   ', '12-bit     ')
    print('--------', '------------')
    print(eight_bit_passwd(), twelve_bit_passwd())
