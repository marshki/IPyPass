#!/usr/bin/env python3

try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk

def eight_bit_passwd(ip_address_in):
    """Transform IP address to 8-bit password.
    """

    split_address = ip_address_in.split('.', 4)

    return((split_address[2] + '*' +
            str(int(split_address[3]) + 8)).ljust(8, '*'))

def twelve_bit_passwd(ip_address_in):
    """Transform IP address to 12-bit password.
    """

    split_address = ip_address_in.split('.', 4)

    return((split_address[2] + '*' +
            str(int(split_address[3]) + 12) + '*' + split_address[1]).ljust(12, '*'))

class MainWindow(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.config(menu=MenuBar(self))

class MenuBar(tk.Menu):
    def __init__(self, master):
        tk.Menu.__init__(self, master)

        file_menu = tk.Menu(self, tearoff=False)
        self.add_cascade(label='File', menu=file_menu)
        #file_menu.add_command(label='F to C mode', command=master.f2c_mode)
        #file_menu.add_command(label='C to F mode', command=master.c2f_mode)
        file_menu.add_separator()
        file_menu.add_command(label='Exit', command=self.quit)

def main():
    window = tk.Tk()
    window.title("IPyPass")
    frame = MainWindow(window)
    frame.pack()
    window.mainloop()

if __name__ == '__main__':
    main()
