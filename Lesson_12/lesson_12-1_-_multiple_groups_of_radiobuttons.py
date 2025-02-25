from tkinter import *

class MyFrame(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.geometry("300x200")
        self.master.title("Text Sampler")
        self.grid()

        self.sample_label = Label(self, text="Some Sample Text", font = "Courier 10")
        self.sample_label.grid(row = 0, column = 0, columnspan = 2)

        self.bold_on = IntVar()
        self.check_bold = Checkbutton(self, text = "Bold",
                variable = self.bold_on, command = self.set_font)
        self.check_bold.grid(row = 1, column = 0)

        self.underline_on = IntVar()
        self.check_underline = Checkbutton(self, text = "Underline",
                variable = self.underline_on, command = self.set_font)
        self.check_underline.grid(row = 1, column = 1)

        self.point_size = StringVar()
        self.point_size.set("10")
        self.ten_point = Radiobutton(self, text = "10 point",
                variable = self.point_size, value = "10",
                command = self.set_font)
        self.ten_point.grid(row = 2, column = 0)

        self.twelve_point = Radiobutton(self, text = "12 point",
                variable = self.point_size, value = "12",
                command = self.set_font)
        self.twelve_point.grid(row = 2, column = 1)

        self.family = StringVar()
        self.times = Radiobutton(self, text = "Times",
            variable = self.family, value = "times",
            command = self.set_font)
        self.times.grid(row = 3, column = 0)
        self.courier = Radiobutton(self, text = "Courier",
            variable = self.family, value = "courier",
            command = self.set_font)
        self.courier.grid(row = 3, column = 1)

    def set_font(self):
        if self.family.get() == "times":
            new_font = "Courier "
        else:
            new_font = "Times "

        if self.point_size.get() == "10":
            new_font = new_font + " 10"
        else:
            new_font = new_font + " 12"
    
        if self.bold_on.get() == 1:
            new_font = new_font + " bold"

        if self.underline_on.get() == 1:
            new_font = new_font + " underline"
      
        self.sample_label.config( font = new_font)

frame04 = MyFrame()
frame04.mainloop()
