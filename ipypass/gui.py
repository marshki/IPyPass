from tkinter import *

class Window(Frame):


    def __init__(self, master=None):
        Frame.__init__(self, master)                 
        self.master = master
        self.init_window()

    #Creation of init_window
    def init_window(self):

        self.master.title("IPyPass")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a button instance
        quitButton = Button(self, text="Derp!")

        # placing the button on window
        quitButton.place(x=0, y=0)

root = Tk()

#size of the window
root.geometry("400x300")

app = Window(root)
root.mainloop()  
