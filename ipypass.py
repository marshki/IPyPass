#!/usr/bin/env python3

"""Take IPv4 address and return 8- or 12-character passwords."""

import argparse
import ipaddress
import logging

def parse_cli_args(arguments=None):
    """Command line parser for IPv4 address of interest, with validation.

    Returns:
        IPv4 address as an instance of ipaddress.IPv4Address.

    Raises:
        argparse.ArgumentTypeError: If the IP address is invalid.
    """
    parser = argparse.ArgumentParser(description="IPv4 address of interest.")
    parser.add_argument("--ip", action="store", type=ipaddress.IPv4Address,
                        required=False, help="IP address of interest, e.g. 0.0.0.0")

    arguments = parser.parse_args(arguments)

    return arguments.ip if hasattr(arguments, 'ip') else None

def eight_char_passwd(split_address):
    """Transform IP address to 8-character password.

    Args:
        split_address: List containing the four octets of the IP address.

    Returns:
        8-character password.
    """
    return (split_address[2] + '*' +
            str(int(split_address[3]) + 8)).ljust(8, '*')

def twelve_char_passwd(split_address):
    """Transform IP address to 12-character password.

    Args:
        split_address: List containing the four octets of the IP address.

    Returns:
        12-character password.
    """
    return (split_address[2] + '*' +
            str(int(split_address[3]) + 12) + '*' +
            split_address[1]).ljust(12, '*')

def create_table(ip_address):
    """Create a crude table.

    Args:
        ip_address: The IP address.

    Prints:
        Table with transformed output.
    """
    split_address = str(ip_address).split('.')
    print('8-char  ', '12-char    ')
    print('--------', '------------')
    print(eight_char_passwd(split_address), twelve_char_passwd(split_address))

def ipypass():
    """Transform IPv4 address to 8- or 12-character password (GUI).

    Returns:
        8- and 12-character passwords.
    """
    # Import tkinter here so CLI works on systems without Tk.
    import tkinter as tk  # pylint: disable=import-outside-toplevel
    def on_convert():
        ip_address = ip_address_entry.get()
        try:
            address = ipaddress.IPv4Address(ip_address)
            split_address = str(address).split('.')
            eight_char = eight_char_passwd(split_address)
            twelve_char = twelve_char_passwd(split_address)
        except ValueError as exception:
            logging.exception(exception)
            eight_char = 'Invalid input.'
            twelve_char = 'Try again.'
        eight_char_label.config(text=eight_char)
        twelve_char_label.config(text=twelve_char)

    root = tk.Tk()
    root.title("IPyPass")

    tk.Label(root, text="Enter IP address:").pack()
    ip_address_entry = tk.Entry(root)
    ip_address_entry.pack()

    convert_button = tk.Button(root, text="Convert", command=on_convert)
    convert_button.pack()

    eight_char_label = tk.Label(root, text="", width=16)
    eight_char_label.pack()

    twelve_char_label = tk.Label(root, text="", width=16)
    twelve_char_label.pack()

    root.mainloop()

def main():
    """Run CLI if IP address is given, otherwise run GUI."""
    args = parse_cli_args()

    if args is not None:
        create_table(args)
    else:
        ipypass()

if __name__ == '__main__':
    main()
