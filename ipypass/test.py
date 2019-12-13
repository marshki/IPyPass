#!/usr/bin/env python3

import PySimpleGUI as sg

sg.change_look_and_feel('Reddit')

LAYOUT = [[sg.Txt('Enter IP address:')],
          [sg.In(size=(16, 1), key='IP_ADDRESS')],
          [sg.Txt('', size=(16, 1), key='output')],
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

            CALC = eight_bit_passwd()
        except:
            CALC = 'Invalid'

        window['output'].update(CALC)
    else:
        break
