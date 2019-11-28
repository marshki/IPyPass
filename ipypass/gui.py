#!/usr/bin/env python3

import tkinter as tk

def eight_bit_passwd(address):
    """Transform IP address to 8-bit password.
    """

    split_address = address.split('.', 4)

    return((split_address[2] + '*' +
            str(int(split_address[3]) + 8)).ljust(8, '*'))

def twelve_bit_passwd(address):
    """Transform IP address to 12-bit password.
    """

    split_address = address.split('.', 4)

    return((split_address[2] + '*' +
            str(int(split_address[3]) + 12) + '*' + split_address[1]).ljust(12, '*'))


class MainWindow(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.config(menu=MenuBar(self))


print(eight_bit_passwd("216.165.95.149"))
print(twelve_bit_passwd("216.165.95.149"))
