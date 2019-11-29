#!/usr/bin/env python
# pylint: disable=too-many-ancestors

"""GUI implementation for IPyPass.
"""

try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk

def eight_bit_passwd(address_in):
    """Transform IP address to 8-bit password.
    """

    split_address = address_in.split('.', 4)

    return((split_address[2] + '*' +
            str(int(split_address[3]) + 8)).ljust(8, '*'))

def twelve_bit_passwd(address_in):
    """Transform IP address to 12-bit password.
    """

    split_address = address_in.split('.', 4)

    return((split_address[2] + '*' +
            str(int(split_address[3]) + 12) + '*' + split_address[1]).ljust(12, '*'))

class MainWindow(tk.Frame):
    """Main window class.
    """

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.config(menu=MenuBar(self))

        self.mode = 'eightbit'

        self.label_in = tk.Label(self, text='IP Address:')
        self.label_in.pack()

        self.ip_in = tk.StringVar(0)

        text = tk.Entry(self, textvar=self.ip_in)
        text.pack()

        self.ip_out = tk.StringVar(self, '0*8*****')
        lbl = tk.Label(self, textvar=self.ip_out)
        lbl.pack()

        btn = tk.Button(self, text='Convert', command=self.convert)
        btn.pack()

        btn = tk.Button(self, text='Quit', command=master.destroy)
        btn.pack()

        def convert(self):
            #self.mode == 'eightbit':
            ip_out = eight_bit_passwd(self.ip_in.get())

class MenuBar(tk.Menu):
    """Menu bar class.
    """

    def __init__(self, master):
        tk.Menu.__init__(self, master)

        file_menu = tk.Menu(self, tearoff=False)
        self.add_cascade(label='File', menu=file_menu)
        file_menu.add_command(label='8-bit mode')#, command=master.f2c_mode)
        file_menu.add_command(label='12-bit mode')#, command=master.c2f_mode)
        file_menu.add_separator()
        file_menu.add_command(label='Exit', command=self.quit)

def main():
    """Main function.
    """

    window = tk.Tk()
    window.title("IPyPass")
    frame = MainWindow(window)
    frame.pack()
    window.mainloop()

if __name__ == '__main__':
    main()
