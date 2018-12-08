import tkinter as tk
import PIL.Image as Image
import PIL.ImageTk as ImageTk
from main_window_backEnd import *


class Window:
    def __init__(self):

        self.picturesList = []
        self.mainWin = tk.Tk()

        # Create 4 main frames
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

        # --------------FRAME 1-------------------------
        # ---List containing small photos in frame 1---
        self.photo_button_List = []

        # ----Add Photo Button----
        self.addPhotoButton = tk.Button(self.frame1, text="+", font="Arial 32 bold",
                                        height=1, width=3, relief=tk.RIDGE,
                                        command=self.selectFilesDialogue)
        self.addPhotoButton.grid(row=0, column=0, padx=10, pady=10)

        # --------------FRAME 2 --------------------------
        # Label of displaying selected picture
        self.displayLabel = tk.Label(self.frame2, relief=tk.GROOVE)
        self.grid(row=0, column=0, justify=tk.CENTER)

    def selectFilesDialogue(self):
        """
        create a dialogue window to prompt the users to selects image files to process.
            :param rootWindow: (window) the root window
            :return: (list) list of the path to the selected files
        """
        # Diaglogue window to select files
        files_Path = filedialog.askopenfilenames(parent=self.mainWin, title='Choose a file')
        selected_Files = self.mainWin.tk.splitlist(files_Path)

        # Need to assign all the images into a self.pictureList so that python garbage collector won't wipe data.
        for j in selected_Files:
            self.picturesList.append(Photo(j))  # Photo object that contain an image file and

        # Create buttons displaying all images

        for i in range(len(self.picturesList)):
            self.photo_button_List.append(tk.Button(self.frame1, image=self.picturesList[i].thumbnailForButton))
            self.photo_button_List[i].configure(width=100, height=100, relief=tk.FLAT, bd=0, )
            self.photo_button_List[i].grid(row=i // 3, column=i % 3 + 1, padx=5, pady=5)


    def display(self, photo):
        tk.Label(self.frame2, image = photo, relief=tk.GROOVE)


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

    img1 = tk.Button(frame1, text="+", font="Arial 32 bold", relief=tk.GROOVE, command=selectFilesDialogue(mainWin))
    img1.grid(row=0, column=0, padx=10, pady=10)

    mainWin.mainloop()


def test():
    pass


if __name__ == '__main__':
    window1 = Window()
    window1.run()

    # test()

    # version()
