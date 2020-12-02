#!/usr/bin/env python3
#pylint: disable=C0103
#pylint: disable=W0703

"""Take IPv4 address and return 8- or 12-bit password (GUI)."""

import logging
import PySimpleGUI as sg

sg.change_look_and_feel('Reddit')

LAYOUT = [[sg.Txt('Enter IP address:')],
          [sg.In(size=(16, 1), key='ip_address')],
          [sg.Txt('', size=(16, 1), key='output_1')],
          [sg.Txt('', size=(16, 1), key='output_2')],
          [sg.Button('Convert', bind_return_key=True)]]

Window = sg.Window('IPyPass', LAYOUT)

def ipypass():
    """
    Transform IPv4 address to 8- or 12-bit password.

    Args: IPv4 address of the form: 0.0.0.0
    Returns: 8- and 12-bit passwords.

    """
    while True:
        event, values = Window.read()

        if event is not None:
            try:
                ip_address = str(values['ip_address'])
                split_address = ip_address.split('.', 4)

                def eight_bit_passwd():
                    """
                    Transform IP address to 8-bit password.

                    Args: String-converted IPv4 address, split by octet.
                    Returns: 8-bit password.

                    """
                    return((split_address[2] + '*' +
                            str(int(split_address[3]) + 8)).ljust(8, '*'))

                def twelve_bit_passwd():
                    """
                    Transform IP address to 12-bit password.

                    Args: String-converted IPv4 address, split by octet.
                    Returns: 12-bit password.

                    """
                    return((split_address[2] + '*' +
                            str(int(split_address[3]) + 12) + '*'
                            + split_address[1]).ljust(12, '*'))

                eight_bit = eight_bit_passwd()
                twelve_bit = twelve_bit_passwd()

            except Exception as e:
                logging.exception(e)

                eight_bit = 'Invlid input.'
                twelve_bit = 'Try again.'

            Window['output_1'].update(eight_bit)
            Window['output_2'].update(twelve_bit)

        else:
            break

if __name__ == '__main__':
    ipypass()
