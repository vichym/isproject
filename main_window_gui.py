import tkinter as tk
import PIL.Image as Image
import PIL.ImageTk as ImageTk


class Window1:
    def __init__(self):
        self.mainWin = tk.Tk()
        self.mainWin.geometry("1250x600")

        FileImage = Image.open("SampleImages/ImageFile.png")
        self.file1Image = ImageTk.PhotoImage(FileImage)

        plusImage = Image.open("SampleImages/PlusImage2.png")
        self.PlusIma = ImageTk.PhotoImage(plusImage)

        label1 = tk.Button(self.mainWin, image=self.PlusIma, height=250, width=300)
        label1.grid(row=0, column=0)

        label2 = tk.Button(self.mainWin, image=self.file1Image, height=250, width=300)
        label2.grid(row=0, column=1)

        label3 = tk.Button(self.mainWin, image=self.file1Image, height=250, width=300)
        label3.grid(row=0, column=2)

        label4 = tk.Button(self.mainWin, image=self.file1Image, height=250, width=300)
        label4.grid(row=0, column=3)

        label5 = tk.Button(self.mainWin, image=self.file1Image, height=250, width=300)
        label5.grid(row=1, column=0)



    def run(self):
        self.mainWin.mainloop()


# myGui = Window1()
# myGui.run()

class Window2:
    def __init__(self):
        self.mainWin = tk.Tk()
        self.mainWin.geometry("1250x600")
        # FRAME 1
        self.frame1 = tk.Frame(self.mainWin, padx=150, pady=50, highlightthickness=1, highlightbackground='black')
        self.frame1.grid(row=0, column=0, sticky='N' + 'W')

        pic = Image.open("download.jpg")
        self.pic = ImageTk.PhotoImage(pic)

        self.img1 = tk.Button(self.frame1, image=self.pic, width=100, height=100)
        self.img1.grid(row=0, column=0)
        space = tk.Label(self.frame1, width=2).grid(row=0, column=1)

        self.img2 = tk.Button(self.frame1, image=self.pic, width=100, height=100)
        self.img2.grid(row=0, column=2)
        space = tk.Label(self.frame1, width=2).grid(row=0, column=3)

        self.img3 = tk.Button(self.frame1, image=self.pic, width=100, height=100)
        self.img3.grid(row=0, column=4)
        space = tk.Label(self.frame1, width=2).grid(row=0, column=5)

        self.img4 = tk.Button(self.frame1, image=self.pic, width=100, height=100)
        self.img4.grid(row=0, column=6)
        space = tk.Label(self.frame1, height=1).grid(row=1, column=0)

        self.img5 = tk.Button(self.frame1, image=self.pic, width=100, height=100)
        self.img5.grid(row=2, column=0)
        space = tk.Label(self.frame1, width=2).grid(row=1, column=1)

        self.img6 = tk.Button(self.frame1, image=self.pic, width=100, height=100)
        self.img6.grid(row=2, column=2)
        space = tk.Label(self.frame1, width=2).grid(row=1, column=3)

        self.img7 = tk.Button(self.frame1, image=self.pic, width=100, height=100)
        self.img7.grid(row=2, column=4)
        space = tk.Label(self.frame1, width=2).grid(row=1, column=5)

        self.img8 = tk.Button(self.frame1, text="+", font="Arial 32 bold", width=4, height=1, relief=tk.GROOVE)
        self.img8.grid(row=2, column=6)

        self.scrollbarF1 = tk.Scrollbar(self.frame1).grid(row=0, column=7)

        # Frame 2
        self.frame2 = tk.Frame(self.mainWin, padx=150, pady=64, highlightthickness=1, highlightbackground='black')
        self.frame2.grid(row=0, column=1, sticky='E' + 'N')

        self.mainPic = tk.Label(self.frame2, image=self.pic, width=200, height=200)
        self.mainPic.grid(row=0, column=0)

    def getProjectName(self):
        inputProjectName = tk.simpledialog.askstring("Input Project Name", "How do you like to name your project?",
                                                     parent=self.mainWin)
        return inputProjectName

    def run(self):
        self.mainWin.mainloop()


myGui = Window2()
myGui.run()
