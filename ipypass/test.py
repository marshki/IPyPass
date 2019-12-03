#!/usr/bin/env python

from Tkinter import *

root = Tk()
show=Label(root, text="|IPyPass|")
show.pack()
show1=Label(root,text="_______________________")
show1.pack()


textlab1=Label(root, text="Enter IP address:")
textlab1.pack()
e1 = Entry(root)
e1.pack()

l = Label(root)

def callback():
    total = sum(int(e.get()) for e in (e1, e2))
    l.config(text="Answer = %s" % total)

b = Button(root, text="Convert", command=callback)

for widget in (e1, l, b):
    widget.pack()
b.mainloop()
