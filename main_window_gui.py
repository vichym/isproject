import tkinter as tk
import PIL
import PIL.Image as Image
import PIL.ImageTk as ImageTk

class Window1:
    def __init__(self):
        self.mainWin = tk.Tk()
        self.mainWin.geometry("1250x600")
        label1 = tk.Label(self.mainWin, text="+", font="Arial 32 bold",height = 5, width = 10, borderwidth = 50)
        label1.grid(row=0, column=0)

        FileImage = Image.open("SampleImages/ImageFile.png")
        self.file1Image = ImageTk.PhotoImage(FileImage)
        label2 = tk.Label(self.mainWin, image = self.file1Image)
        label2.grid(row=0, column=1)

        label3 = tk.Label(self.mainWin, image = self.file1Image)
        label3.grid(row=0, column=2)

        label4 = tk.Label(self.mainWin, image = self.file1Image)
        label4.grid(row=0, column=3)

        label5 = tk.Label(self.mainWin, image = self.file1Image)
        label5.grid(row=1, column=0)
    def run(self):
        self.mainWin.mainloop()


myGui = Window1()
myGui.run()