import tkinter as tk
import PIL.Image as Image
import PIL.ImageTk as ImageTk

class Window1:
    def __init__(self):
        self.mainWin = tk.Tk()
        self.mainWin.geometry("1000x600")

        FileImage = Image.open("SampleImages/ImageFile.png")
        self.file1Image = ImageTk.PhotoImage(FileImage)

        plusImage = Image.open("SampleImages/PlusImage2.png")
        self.PlusIma = ImageTk.PhotoImage(plusImage)

        label1 = tk.Button(self.mainWin, image = self.PlusIma, height = 250, width = 241)
        label1.grid(row=0, column=0)

        label2 = tk.Button(self.mainWin, image = self.file1Image, height = 250, width = 241)
        label2.grid(row=0, column=1)

        label3 = tk.Button(self.mainWin, image = self.file1Image, height = 250, width = 241)
        label3.grid(row=0, column=2)

        label4 = tk.Button(self.mainWin, image = self.file1Image, height = 250, width = 241)
        label4.grid(row=0, column=3)

        label5 = tk.Button(self.mainWin, image = self.file1Image, height = 250, width =241)
        label5.grid(row=1, column=0)


    def run(self):
        self.mainWin.mainloop()


myGui = Window1()
myGui.run()