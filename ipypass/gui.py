#!/usr/bin/env python3

#import Tkinter as tk

def eight_bit_passwd(address):
    """Transform IP address to 8-bit password.
    """

    split_address = address.split('.', 4)

    return((split_address[2] + '*' +
            str(int(split_address[3]) + 8)).ljust(8, '*'))

print(eight_bit_passwd("216.165.95.149"))
