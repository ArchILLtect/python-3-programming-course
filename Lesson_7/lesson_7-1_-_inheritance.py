from tkinter import *

class MyFrame(Frame):
    """A Frame Class"""
    def __init__(self):
        Frame.__init__(self)

        self.myCanvas = Canvas(width=300, height=200, bg="blue")
        self.myCanvas.grid()
        
        self.myCanvas.create_rectangle(10, 10, 50, 50, fill="red", outline="purple", width=5)
        self.myCanvas.create_text(10, 55, text="Hi there!", anchor="nw")
        

# Now create a MyFrame object and call on mainloop
frame02 = MyFrame()
frame02.mainloop()
