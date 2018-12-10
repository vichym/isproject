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





class Window2:
    def __init__(self):
        self.mainWin = tk.Tk()

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


        # Frame 2
        self.frame2 = tk.Frame(self.mainWin, padx=100, pady=15, highlightthickness=1, highlightbackground='black')
        self.frame2.grid(row=0, column=1, sticky='E' + 'N')

        self.mainPic = tk.Label(self.frame2, image=self.pic, width=300, height=300)
        self.mainPic.grid(row=0, column=0)

        #Frame 3
        self.frame3 = tk.Frame(self.mainWin, padx=176,pady=26,highlightthickness=1, highlightbackground='black')
        self.frame3.grid(row=1,column=0,sticky= 'S'+'W')

        self.filter1 = tk.Button(self.frame3, image=self.pic, width=80, height=80)
        self.filter1.grid(row=0, column=0, padx=5)

        self.filter2 = tk.Button(self.frame3, image=self.pic, width=80, height=80)
        self.filter2.grid(row=0, column=2,padx=5)

        self.filter3 = tk.Button(self.frame3, image=self.pic, width=80, height=80)
        self.filter3.grid(row=0, column=4,padx=5)

        self.filter4 = tk.Button(self.frame3, image=self.pic, width=80, height=80)
        self.filter4.grid(row=2, column=0,padx=5)

        self.filter5 = tk.Button(self.frame3, image=self.pic, width=80, height=80)
        self.filter5.grid(row=2, column=2,padx=5)

        self.filter6 = tk.Button(self.frame3, image=self.pic, width=80, height=80)
        self.filter6.grid(row=2, column=4,padx=5)

        # use just like Entry widget (self.scaleRED.get() etc.)
        self.scaleRED = tk.Scale(self.frame3, from_=0,to_=255,orient='horizontal', label ='RED')
        self.scaleRED.grid(row=0,column=6)

        self.scaleGREEN = tk.Scale(self.frame3, from_=0, to_=255, orient='horizontal',label='GREEN')
        self.scaleGREEN.grid(row=1, column=6)

        self.scaleBLUE = tk.Scale(self.frame3, from_=0, to_=255, orient='horizontal',label='BLUE')
        self.scaleBLUE.grid(row=2, column=6)

        #Frame 4:
        self.frame4=tk.Frame(self.mainWin, padx=150, pady=38, highlightthickness=1, highlightbackground='black')
        self.frame4.grid(row=1,column=1,sticky='E'+'S')

        plusImage = Image.open("SampleImages/PlusImage2.png")
        self.PlusIma = ImageTk.PhotoImage(plusImage)
        #will delete 3 lines above once we combine 2 classes (win1 and win2)
        self.stamp=tk.Button(self.frame4, image=self.PlusIma, width=200, height=200)
        self.stamp.grid(row=0,column=0)

    def run(self):
        self.mainWin.mainloop()

if __name__ == '__main__':
    # myGui = Window1()
    # myGui.run()
    myGui = Window2()
    myGui.run()
