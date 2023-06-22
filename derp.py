#!/usr/bin/env python3

"""IPv4 validation using `ipaddress module` and argparse."""

import argparse
import ipaddress
import unittest

from ipaddress import IPv4Address
from unittest.mock import patch

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
        IPv4 address as an instance of ipaddress.IPv4Address, or None if no IP address is provided.

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

class IPyPassTests(unittest.TestCase):
    """Unit tests."""

    @patch('sys.argv', ['script_name', '--ip', '192.168.0.1'])
    def test_parse_cli_args(self):
        ip = parse_cli_args()
        self.assertIsInstance(ip, IPv4Address)
        self.assertEqual(str(ip), '192.168.0.1')

    @patch('sys.argv', ['script_name'])
    def test_parse_cli_args_no_ip(self):
        ip = parse_cli_args()
        self.assertIsNone(ip)

    def test_eight_bit_passwd(self):
        split_address = ['192', '168', '0', '1']
        password = eight_bit_passwd(split_address)
        self.assertEqual(password, '0*9*****')

    def test_twelve_bit_passwd(self):
        split_address = ['192', '168', '0', '1']
        password = twelve_bit_passwd(split_address)
        self.assertEqual(password, '0*13*168****')

    def test_create_table(self):
        ip_address = IPv4Address('192.168.0.1')
        expected_output = '8-bit    12-bit     \n-------- ------------\n0*9***** 0*13*168****\n'
        with redirect_stdout(StringIO()) as output:
            create_table(ip_address)
            self.assertEqual(output.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
