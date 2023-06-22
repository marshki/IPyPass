#!/usr/bin/env python3

"""Take IPv4 address and return 8- or 12-bit passwords."""

import argparse
import ipaddress
import logging
import PySimpleGUI as sg

sg.change_look_and_feel('Reddit')

LAYOUT = [[sg.Txt('Enter IP address:')],
          [sg.In(size=(16, 1), key='ip_address')],
          [sg.Txt('', size=(16, 1), key='output_1')],
          [sg.Txt('', size=(16, 1), key='output_2')],
          [sg.Button('Convert', bind_return_key=True)]]

Window = sg.Window('IPyPass', LAYOUT)


def parse_cli_args():
    """
    Command line parser for IPv4 address of interest, with validation.

    Returns:
        IPv4 address as an instance of ipaddress.IPv4Address.

    Raises:
        argparse.ArgumentTypeError: If the IP address is invalid.
    """

    parser = argparse.ArgumentParser(description="IPv4 address of interest.")
    parser.add_argument("--ip", action="store", type=ipaddress.IPv4Address,
                        required=False,
                        help="IP address of interest, e.g. 0.0.0.0")
    args = parser.parse_args()

    return args.ip

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
    while True:
        event, values = Window.read()

        if event == sg.WINDOW_CLOSED:
            break

        if event == 'Convert':
            try:
                ip_address = str(values['ip_address'])
                address = ipaddress.IPv4Address(ip_address)
                split_address = str(address).split('.')
                eight_bit = eight_bit_passwd(split_address)
                twelve_bit = twelve_bit_passwd(split_address)

            except Exception as e:
                logging.exception(e)
                eight_bit = 'Invalid input.'
                twelve_bit = 'Try again.'

            Window['output_1'].update(eight_bit)
            Window['output_2'].update(twelve_bit)


if __name__ == '__main__':
    args = parse_cli_args()

    if args is not None:
        create_table(args)
    else:
        ipypass()
