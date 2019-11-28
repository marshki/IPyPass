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

        self.mode = 'eightbit'

        self.label_in = tk.Label(self, text='Enter IP address:')
        self.label_in.pack()

        self.ip_in = tk.DoubleVar(0)
        text = tk.Entry(self, textvar=self.ip_in)
        text.pack()

        self.ip_out = tk.StringVar(self, '0*8*****')
        lbl = tk.Label(self, textvar=self.ip_out)
        lbl.pack()

        btn = tk.Button(self, text='Convert', command=self.convert)
        btn.pack()

        btn = tk.Button(self, text='Quit', command=master.destroy)
        btn.pack()

    def eight_bit_mode(self):
        self.mode = 'eightbit'
        self.label_in.config(text='8-bit password:')

    def twelve_bit_mode(self):
        self.mode = 'twelvebit'
        self.label_in.config(text='12-bit password:') 

    def convert(self):
        try:
            if self.mode == 'eightbit':
                ip_out = eight_bit_passwd(self.ip_in.get())
            else:
                ip_out = twelve_bit_passwd(self.temp_in.get())
            self.ip_out.set("{:.3f}".format(ip_out))
        except ValueError as e:
            self.ip_out.set("ERROR: {}".format(e))

class MenuBar(tk.Menu):
    def __init__(self, master):
        tk.Menu.__init__(self, master)

        file_menu = tk.Menu(self, tearoff=False)
        self.add_cascade(label='File', menu=file_menu)
        file_menu.add_command(label='8 bit mode', command=master.eight_bit_mode)
        file_menu.add_command(label='12 bit mode', command=master.twelve_bit_mode)
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
