#!/usr/bin/env python3

"""Take IPv4 address and return 8- or 12-bit passwords."""

import argparse
import ipaddress
import logging
import tkinter as tk

def parse_cli_args(args=None):
    """
    Command line parser for IPv4 address of interest, with validation.

    Returns:
        IPv4 address as an instance of ipaddress.IPv4Address.

    Raises:
        argparse.ArgumentTypeError: If the IP address is invalid.
    """
    parser = argparse.ArgumentParser(description="IPv4 address of interest.")
    parser.add_argument("--ip", action="store", type=ipaddress.IPv4Address,
                        required=False, help="IP address of interest, e.g. 0.0.0.0")

    args = parser.parse_args(args)

    return args.ip if hasattr(args, 'ip') else None

def eight_bit_passwd(split_address):
    """
    Transform IP address to 8-bit password.

    Args:
        split_address: List containing the four octets of the IP address.

    Returns:
        8-bit password.
    """
    return (split_address[2] + '*' +
            str(int(split_address[3]) + 8)).ljust(8, '*')

def twelve_bit_passwd(split_address):
    """
    Transform IP address to 12-bit password.

    Args:
        split_address: List containing the four octets of the IP address.

    Returns:
        12-bit password.
    """
    return (split_address[2] + '*' +
            str(int(split_address[3]) + 12) + '*' +
            split_address[1]).ljust(12, '*')

def create_table(ip_address):
    """
    Create a crude table.

    Args:
        ip_address: The IP address.

    Prints:
        Table with transformed output.
    """
    split_address = str(ip_address).split('.')
    print('8-bit   ', '12-bit     ')
    print('--------', '------------')
    print(eight_bit_passwd(split_address), twelve_bit_passwd(split_address))

def ipypass():
    """
    Transform IPv4 address to 8- or 12-bit password (GUI).

    Returns:
        8- and 12-bit passwords.
    """
    def on_convert():
        ip_address = ip_address_entry.get()
        try:
            address = ipaddress.IPv4Address(ip_address)
            split_address = str(address).split('.')
            eight_bit = eight_bit_passwd(split_address)
            twelve_bit = twelve_bit_passwd(split_address)
        except ValueError as e:
            logging.exception(e)
            eight_bit = 'Invalid input.'
            twelve_bit = 'Try again.'
        eight_bit_label.config(text=eight_bit)
        twelve_bit_label.config(text=twelve_bit)

    root = tk.Tk()
    root.title("IPyPass")

    tk.Label(root, text="Enter IP address:").pack()
    ip_address_entry = tk.Entry(root)
    ip_address_entry.pack()

    convert_button = tk.Button(root, text="Convert", command=on_convert)
    convert_button.pack()

    eight_bit_label = tk.Label(root, text="", width=16)
    eight_bit_label.pack()

    twelve_bit_label = tk.Label(root, text="", width=16)
    twelve_bit_label.pack()

    root.mainloop()

if __name__ == '__main__':
    args = parse_cli_args()

    if args is not None:
        create_table(args)
    else:
        ipypass()
