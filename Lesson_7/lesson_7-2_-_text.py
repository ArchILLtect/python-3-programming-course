from tkinter import *

class MyFrame(Frame):
    def __init__(self):
        Frame.__init__(self)

        self.myCanvas = Canvas(width=300, height=200, bg="blue")

        self.myCanvas.create_rectangle(10, 10, 200, 100, fill="blue")
        self.myCanvas.create_oval(10, 10, 200, 100, fill="white")

        self.myCanvas.create_line(1, 1, 200, 200, arrow="first")
        self.myCanvas.create_text(50, 50, text="Hello World")

        self.myCanvas.grid()

frame02 = MyFrame()
frame02.mainloop()
