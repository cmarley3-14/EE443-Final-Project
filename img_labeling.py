from tkinter import *
from PIL import Image, ImageTk

class App(Frame):
    def __init__(self, master):
        super().__init__()
        self.master = master

        self.labels = [0]*400
        self.counter = 0

        self.canvas_l = Canvas(self.master, height=250, width=250,
                               bg = '#eeeeff', highlightthickness=0)
        self.canvas_l.grid()
        self.canvas_r = Canvas(self.master, height=250, width=250,
                               bg = '#eeffee', highlightthickness=0)
        self.canvas_r.grid(row=0, column=1)

        self.img_l = ImageTk.PhotoImage(Image.open("test_000_0.jpg"))
        self.canvas_l.create_image(0,0, anchor=NW, image=self.img_l)
        self.img_r = ImageTk.PhotoImage(Image.open("test_000_1.jpg"))
        self.canvas_r.create_image(0,0, anchor=NW, image=self.img_r)

        self.master.bind("y", self.advance)
        self.master.bind("n", self.advance)

    def advance(self, event):
        with open("labels.txt", 'a') as infile:
            infile.write(event.char + "\n")
        self.counter += 1
        self.img_l = ImageTk.PhotoImage(Image.open(f"test_{self.counter:03}_0.jpg"))
        self.img_r = ImageTk.PhotoImage(Image.open(f"test_{self.counter:03}_1.jpg"))
        self.canvas_l.create_image(0,0, anchor=NW, image=self.img_l)
        self.canvas_r.create_image(0,0, anchor=NW, image=self.img_r)

root = Tk()
myApp = App(root)
myApp.mainloop()
