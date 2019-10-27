#!/usr/bin/env python3

"""Take IPv4 addresss and return 8- or 12-bit password.
"""

import ipaddress

def ipv4_addr_check():
    """Prompt user for IPv4 address, then validate.
    """

    while True:
        try:
            return str(ipaddress.IPv4Address(input('Enter valid IPv4 address: ')))
        except ValueError:
            print('Bad value, try again.')

def eight_bit_passwd():
    """Transform IP address to 8-bit password.
    """
    return((SPLIT_ADDRESS[2] + '*' +
            str(int(SPLIT_ADDRESS[3]) + 8)).ljust(8, '*'))

def twelve_bit_passwd():
    """Transform IP address to 12-bit password.
    """
    return((SPLIT_ADDRESS[2] + '*' +
            str(int(SPLIT_ADDRESS[3]) + 12) + '*' + SPLIT_ADDRESS[1]).ljust(12, '*'))

if __name__ == '__main__':
    ADDRESS = ipv4_addr_check()
    SPLIT_ADDRESS = ADDRESS.split('.', 4)
    print(eight_bit_passwd())
    print(twelve_bit_passwd())
