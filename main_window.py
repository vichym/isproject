from main_window_backEnd import *


class Window:
    def __init__(self):

        self.picturesList = []
        self.mainWin = tk.Tk()
        self.manipulation = {"filter": '', "stamp": {}, "colorWeight": "{}"}

        # Create 4 main frames
        # TODO: create frame 5 that contain 'process' button at the bottom right corner
        self.frame1 = tk.Frame(self.mainWin, width=700, height=350, background="white", bd=5, relief=tk.SUNKEN)
        self.frame2 = tk.Frame(self.mainWin, width=230, height=350, background="blue", bd=5, relief=tk.GROOVE)
        self.frame3 = tk.Frame(self.mainWin, width=700, height=200, background="Yellow", bd=5)
        self.frame4 = tk.Frame(self.mainWin, width=230, height=200, background="green", bd=5)
        self.frame1.grid(row=0, column=0)
        self.frame2.grid(row=0, column=1)
        self.frame3.grid(row=1, column=0)
        self.frame4.grid(row=1, column=1)
        self.frame1.grid_propagate(0)
        self.frame2.grid_propagate(0)
        self.frame3.grid_propagate(0)
        self.frame4.grid_propagate(0)

        # ====================FRAME 1======================
        # ---List containing small photos in frame 1---
        self.photo_button_List = []

        # ----Add Photo Button----
        self.addPhotoButton = tk.Button(self.frame1, text="+", font="Arial 32 bold",
                                        height=1, width=3, relief=tk.RIDGE,
                                        command=self.selectFilesDialogue)
        self.addPhotoButton.grid(row=0, column=0, padx=10, pady=10)

        # ====================FRAME 2 ========================
        # Label of displaying selected picture
        self.displayLabel = tk.Label(self.frame2, relief=tk.GROOVE)

        self.displayLabel.grid_forget()

        # ====================FRAME 3==========================
        # TODO: creates buttons for filters,

        # 6 filters:
        pic = Image.open("download.jpg")
        self.pic = ImageTk.PhotoImage(pic)

        # https://pillow.readthedocs.io/en/5.1.x/reference/ImageFilter.html
        self.blur = tk.Button(self.frame3, image=self.pic, width=80, height=80)
        self.blur.grid(row=0, column=0, padx=5, pady=5)
        # self.blur.config(command=self.ADD_BLUR_FUNCTION)

        self.contour = tk.Button(self.frame3, image=self.pic, width=80, height=80)
        self.contour.grid(row=0, column=2, padx=5, pady=5)
        # self.contour.config(command=self.ADD)

        self.edgeEnhance = tk.Button(self.frame3, image=self.pic, width=80, height=80)
        self.edgeEnhance.grid(row=0, column=4, padx=5, pady=5)
        # self.edgeEnhance.config(command=self.ADD)

        self.emboss = tk.Button(self.frame3, image=self.pic, width=80, height=80)
        self.emboss.grid(row=2, column=0, padx=5, pady=5)
        # self.emboss.config(command=self.ADD)

        self.sharpen = tk.Button(self.frame3, image=self.pic, width=80, height=80)
        self.sharpen.grid(row=2, column=2, padx=5, pady=5)
        # self.sharpen.config(command=self.ADD)

        self.smooth = tk.Button(self.frame3, image=self.pic, width=80, height=80)
        self.smooth.grid(row=2, column=4, padx=5, pady=5)
        # self.smooth.config(command=self.ADD)

        # the 3 scale widgets
        self.scaleRED = tk.Scale(self.frame3, from_=0, to_=255, orient='vertical',activebackground='red',label='Red')
        self.scaleRED.grid(row=0, column=6, padx=10,rowspan=3)

        self.scaleGREEN = tk.Scale(self.frame3, from_=0, to_=255, orient='vertical',activebackground='green',label='Green')
        self.scaleGREEN.grid(row=0, column=7,padx=10,rowspan=3)

        self.scaleBLUE = tk.Scale(self.frame3, from_=0, to_=255, orient='vertical',activebackground='blue',label='Blue')
        self.scaleBLUE.grid(row=0, column=8,padx=10,rowspan=3)
        # ====================FRAME 4==========================
        # TODO: Create a canvas, and an "Add Stamp" button under that canvas

        # ====================FRAME 5==========================
        # TODO: Create process button on the button right corner.
        self.processButton = tk.Button(self.frame4, text='Proceed', font='Arial 14 bold')
        self.processButton.grid(row=1,column=1,sticky='SE') #will make sense when frame4 is complete lol

    def selectFilesDialogue(self):
        """
        create a dialogue window to prompt the users to selects image files to process.
            :param rootWindow: (window) the root window
            :return: (list) list of the path to the selected files
        """
        # Dialogue windows to select files
        files_Path = filedialog.askopenfilenames(parent=self.mainWin, title='Choose a file')
        selected_Files = self.mainWin.tk.splitlist(files_Path)

        # Need to assign all the images into a self.pictureList before recalling so that python garbage collector won't
        # wipe data.
        for j in selected_Files:
            self.picturesList.append(Photo(j))  # Photo object that contain an image file and

        # Create buttons list displaying all images
        self.photo_button_List.clear()

        # Create Photo Button
        for i in range(len(self.picturesList)):
            self.photo_button_List.append(tk.Button(self.frame1, image=self.picturesList[i].thumbnailForButton))
            self.photo_button_List[i].configure(width=100, height=100, relief=tk.FLAT, bd=0)
            self.photo_button_List[i].grid(row=i // 5, column=i % 5 + 1, padx=5, pady=5)

            # TODO: assign each Button to self.display() to display specific picture on frame 2.
            # Displaying different object by passing parameters to a function
            # Citation:
            self.photo_button_List[i].configure(
                command=lambda x=self.picturesList[i].thumbnailForDisplay: self.display(x))

    def display(self, photo):
        self.displayLabel.configure(image=photo, width=200, height=photo.height())
        self.displayLabel.grid(row=0, column=0, padx=5, pady=10, sticky='swen')

    def run(self):
        self.mainWin.mainloop()


def test():
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


if __name__ == '__main__':
    window1 = Window()
    window1.run()

    # test()

    # version()
