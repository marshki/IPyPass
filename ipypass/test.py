#!/usr/bin/env python3

"""Take IPv4 address and return 8-bit or 12-bit password.
"""

import PySimpleGUI as sg

sg.change_look_and_feel('Reddit')

LAYOUT = [[sg.Txt('Enter IP address:')],
          [sg.In(size=(16, 1), key='IP_ADDRESS')],
          [sg.Txt('', size=(16, 1), key='output_1')],
          [sg.Txt('', size=(16, 1), key='output_2')],
          [sg.Button('Convert', bind_return_key=True)]]

window = sg.Window('IPyPass', LAYOUT)

while True:
    EVENT, VALUES = window.read()

    if EVENT is not None:
        try:
            IP_ADDRESS = str(VALUES['IP_ADDRESS'])
            SPLIT_ADDRESS = IP_ADDRESS.split('.', 4)

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

            EIGHT_BIT = eight_bit_passwd()
            TWELVE_BIT = twelve_bit_passwd()

        except Exception as e:
            EIGHT_BIT = 'Invlid input.'
            TWELVE_BIT = 'Try again.'

        window['output_1'].update(EIGHT_BIT)
        window['output_2'].update(TWELVE_BIT)

    else:
        break
