import tkinter as tk
import PIL.Image as Image
import PIL.ImageTk as ImageTk
from main_window_backEnd import *


class Window:
    def __init__(self):
        self.mainWin = tk.Tk()

        self.frame1 = tk.Frame(self.mainWin, width=600, height=300, background="red", bd=5, relief=tk.SUNKEN)
        self.frame2 = tk.Frame(self.mainWin, width=200, height=300, background="blue", bd=5, relief=tk.GROOVE)
        self.frame3 = tk.Frame(self.mainWin, width=600, height=200, background="Yellow", bd=5)
        self.frame4 = tk.Frame(self.mainWin, width=200, height=200, background="green", bd=5)

        self.frame1.grid(row=0, column=0)
        self.frame2.grid(row=0, column=1)

        self.frame3.grid(row=1, column=0)
        self.frame4.grid(row=1, column=1)

        self.frame1.grid_propagate(0)
        self.frame2.grid_propagate(0)
        self.frame3.grid_propagate(0)
        self.frame4.grid_propagate(0)

        self.buttonList = []
        self.img1 = tk.Button(self.frame1, text="+", font="Arial 32 bold", height=1,width =3, relief=tk.RIDGE,
                              command = self.selectFilesDialogue)
        self.img1.grid(row=0, column=0, padx=10, pady=10)

        # Frame 2
        # self.frame2 = tk.Frame(self.mainWin, padx=150, pady=64, highlightthickness=1, highlightbackground='black')
        # self.frame2.grid(row=0, column=1, sticky='E' + 'N')
        #
        # self.mainPic = tk.Label(self.frame2, image=self.pic, width=200, height=200)
        # self.mainPic.grid(row=0, column=0)

    def selectFilesDialogue(self):
        """
        create a dialogue window to prompt the users to selects image files to process.
            :param rootWindow: (window) the root window
            :return: (list) list of the path to the selected files
        """
        # Diaglogue window to select files
        files = filedialog.askopenfilenames(parent=self.mainWin, title='Choose a file')
        selectedFiles = self.mainWin.tk.splitlist(files)

        # Need to assign all the images into a self.pictureList so that python garbage collector won't wipe data.
        self.picturesList = []
        for j in selectedFiles:
            self.picturesList.append(Photo(j))  # Photo object that contain an image file and

        # Create buttons displaying all images

        for i in range(len(self.picturesList)):
            self.buttonList.append(tk.Button(self.frame1, image=self.picturesList[i].thumbnailVersion))
            self.buttonList[i].configure(width=100, height=100, relief=tk.GROOVE, )
            self.buttonList[i].grid(row=i//3, column=i % 3 + 1, padx=5, pady=5)
            self.buttonList[i].bind()



    def display(self, photo):
        self.displayLabel =tk.Label(self.frame2, image=photo, relief=tk.GROOVE)
        self.displayLabel.grid(row=0, column=0)

        # command = self.display(self.picturesList[i].createThumbnail(200))

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

    img1 = tk.Button(frame1, text="+", font="Arial 32 bold",  relief=tk.GROOVE, command=selectFilesDialogue(mainWin))
    img1.grid(row=0, column=0, padx=10, pady=10)

    mainWin.mainloop()


def test():

    pass

if __name__ == '__main__':
    window1 = Window()
    window1.run()

    # test()

    # version()