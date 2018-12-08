import tkinter as tk
import PIL.Image as Image
import PIL.ImageTk as ImageTk
from main_window_backEnd import *


class Demo1:
    def __init__(self):
        self.mainWin = tk.Tk()

        # FRAM1
        self.frame1 = tk.Frame(self.mainWin, padx=150, pady=50, highlightthickness=1, highlightbackground='black')
        self.frame1.grid(row=0, column=0, sticky='N' + 'W')

        pic = Image.open("download.jpg")
        self.pic = ImageTk.PhotoImage(pic)

        self.img1 = tk.Button(self.frame1, text="+", font="Arial 32 bold", width=4, height=1, relief=tk.GROOVE)
        self.img1.grid(row=0, column=0)
        space = tk.Label(self.frame1, width=2).grid(row=0, column=1)

        # self.img2 = tk.Button(self.frame1, image=self.pic, width=100, height=100)
        # self.img2.grid(row=0, column=2)
        # space = tk.Label(self.frame1, width=2).grid(row=0, column=3)
        #
        # self.img3 = tk.Button(self.frame1, image=self.pic, width=100, height=100)
        # self.img3.grid(row=0, column=4)
        # space = tk.Label(self.frame1, width=2).grid(row=0, column=5)
        #
        # self.img4 = tk.Button(self.frame1, image=self.pic, width=100, height=100)
        # self.img4.grid(row=0, column=6)
        # space = tk.Label(self.frame1, height=1).grid(row=1, column=0)
        #
        # self.img5 = tk.Button(self.frame1, image=self.pic, width=100, height=100)
        # self.img5.grid(row=2, column=0)
        # space = tk.Label(self.frame1, width=2).grid(row=1, column=1)
        #
        # self.img6 = tk.Button(self.frame1, image=self.pic, width=100, height=100)
        # self.img6.grid(row=2, column=2)
        # space = tk.Label(self.frame1, width=2).grid(row=1, column=3)
        #
        # self.img7 = tk.Button(self.frame1, image=self.pic, width=100, height=100)
        # self.img7.grid(row=2, column=4)
        # space = tk.Label(self.frame1, width=2).grid(row=1, column=5)
        #
        # self.img8 = tk.Button(self.frame1, image=self.pic, width=100, height=100)
        #
        # self.img8.grid(row=2, column=6)

        # Frame 2
        self.frame2 = tk.Frame(self.mainWin, padx=150, pady=64, highlightthickness=1, highlightbackground='black')
        self.frame2.grid(row=0, column=1, sticky='E' + 'N')

        self.mainPic = tk.Label(self.frame2, image=self.pic, width=200, height=200)
        self.mainPic.grid(row=0, column=0)

    def new_window(self):
        self.newWindow = tk.Toplevel(self.mainWin)
        self.app = Demo2(self.newWindow)

    def run(self):
        self.mainWin.mainloop()


class Demo2:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.quitButton = tk.Button(self.frame, text='Quit', width=25, command=self.close_windows)
        self.quitButton.pack()
        self.frame.pack()

    def close_windows(self):
        self.master.destroy()


def version():
    mainWin = tk.Tk()
    mainWin.geometry('800x500')

    frame1 = tk.Frame(mainWin, width=600, height=300, background="red", bd=5, relief=tk.SUNKEN)
    frame2 = tk.Frame(mainWin, width=200, height=300, background="blue", bd=5, relief=tk.GROOVE)
    frame3 = tk.Frame(mainWin, width=600, height=200, background="Yellow", bd=5)
    frame4 = tk.Frame(mainWin, width=200, height=200, background="green", bd=5)

    frame1.grid(row=0, column=0)
    frame2.grid(row=0, column=1)

    frame3.grid(row=1, column=0)
    frame4.grid(row=1, column=1)


    frame1.grid_propagate(0)
    frame2.grid_propagate(0)
    frame3.grid_propagate(0)
    frame4.grid_propagate(0)

    img1 = tk.Button(frame1, text="+", font="Arial 32 bold",  relief=tk.GROOVE)
    img1.grid(row=0, column=0, padx=10, pady=10)

    list = selectFilesDialogue(mainWin)

    for i in range(len(list)):
        tk.Button(frame1,text=list[i], width=10, height=5, relief=tk.GROOVE).grid(row= i//6, column=i%6+1,padx=10, pady=10)




    mainWin.mainloop()


def test():
    root = tk.Tk()
    root.geometry("500x300")

    def add():
        tk.Entry(frame).grid()

    def disable():
        frame.configure(height=frame["height"], width=frame["width"])
        frame.grid_propagate(0)

    def enable():
        frame.grid_propagate(1)

    frame = tk.Frame(root, height=100, width=150, bg="black")
    frame.grid(row=1, column=0)

    tk.Button(root, text="add widget", command=add).grid(row=0, column=0)
    tk.Button(root, text="disable propagation", command=disable).grid(row=0, column=1)
    tk.Button(root, text="enable propagation", command=enable).grid(row=0, column=2)

    root.mainloop()


if __name__ == '__main__':
    # window1 = Demo1()
    # window1.run()

    # test()

    version()