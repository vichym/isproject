import os
import tkinter as tk
from tkinter import simpledialog, messagebox

from PIL import ImageFilter

from main_window_backEnd import *


class Window:
    def __init__(self):
        pic = Image.open('download.jpg')
        self.processPhoto_list = []
        self.photosList = []
        self.stampPic = None
        self.mainWin = tk.Tk()
        self.manipulation = {"filter": '', "stamp": {}, "colorWeight": "{}"}

        # Create 4 main frames
        self.frame1 = tk.Frame(self.mainWin, width=700, height=320, background="white", bd=5, relief=tk.SUNKEN)
        self.frame2 = tk.Frame(self.mainWin, width=220, height=320, background="blue", bd=5, relief=tk.GROOVE)
        self.frame3 = tk.Frame(self.mainWin, width=700, height=230, background="Yellow", bd=5)
        self.frame4 = tk.Frame(self.mainWin, width=220, height=230, background="green", bd=5)
        self.frame5 = tk.Frame(self.mainWin, bd=5)
        self.frame1.grid(row=0, column=0)
        self.frame2.grid(row=0, column=1)
        self.frame3.grid(row=1, column=0)
        self.frame4.grid(row=1, column=1)
        self.frame5.grid(row=2, column=1)

        self.frame1.grid_propagate(0)
        self.frame2.grid_propagate(0)
        self.frame3.grid_propagate(0)
        self.frame4.grid_propagate(0)
        self.frame5.grid_propagate(0)

        # ====================FRAME 1======================
        # ---List containing small photos in frame 1---
        self.photo_button_List = []

        # ----Add Photo Button----
        self.addPhoto_Button = tk.Button(self.frame1, text="+", font="Arial 32 bold",
                                         height=1, width=3, relief=tk.RIDGE,
                                         command=self.selectFilesDialogue)
        self.addPhoto_Button.grid(row=0, column=0, padx=10, pady=10)

        # ====================FRAME 2 ========================
        # Label of displaying selected picture
        self.display_Label = tk.Label(self.frame2, relief=tk.GROOVE)

        self.display_Label.grid_forget()

        # ====================FRAME 3==========================

        # 6 filters:

        self.pic = ImageTk.PhotoImage(pic)

        # https://pillow.readthedocs.io/en/5.1.x/reference/ImageFilter.html
        self.blurPic = ImageTk.PhotoImage(pic.filter(ImageFilter.BLUR))
        self.blur = tk.Button(self.frame3, image=self.blurPic, width=90, height=90, text='Blur',compound='center')
        self.blur.grid(row=0, column=0, padx=5, pady=5)
        self.blur.config(command=self.blurFunction)

        self.contourPic = ImageTk.PhotoImage(pic.filter(ImageFilter.CONTOUR))
        self.contour = tk.Button(self.frame3, image=self.contourPic, width=90, height=90, text='Contour', compound='center')
        self.contour.grid(row=0, column=2, padx=5, pady=5)
        self.contour.config(command=self.contourFunction)

        self.edgeEnhancePic = ImageTk.PhotoImage(pic.filter(ImageFilter.EDGE_ENHANCE))
        self.edgeEnhance = tk.Button(self.frame3, image=self.edgeEnhancePic, width=90, height=90, text='Edge Enhance', compound='center')
        self.edgeEnhance.grid(row=0, column=4, padx=5, pady=5)
        self.edgeEnhance.config(command=self.edgeEnhanceFunction)

        self.embossPic = ImageTk.PhotoImage(pic.filter(ImageFilter.EMBOSS))
        self.emboss = tk.Button(self.frame3, image=self.embossPic, width=90, height=90, text = 'Emboss', compound='center')
        self.emboss.grid(row=2, column=0, padx=5, pady=5)
        self.emboss.config(command=self.embossFunction)

        self.sharpenPic = ImageTk.PhotoImage(pic.filter(ImageFilter.SHARPEN))
        self.sharpen = tk.Button(self.frame3, image=self.sharpenPic, width=90, height=90, text='Sharpen', compound='center')
        self.sharpen.grid(row=2, column=2, padx=5, pady=5)
        self.sharpen.config(command=self.sharpenFunction)

        self.smoothPic = ImageTk.PhotoImage(pic.filter(ImageFilter.SMOOTH))
        self.smooth = tk.Button(self.frame3, image=self.smoothPic, width=90, height=90, text='Smooth',compound='center')
        self.smooth.grid(row=2, column=4, padx=5, pady=5)
        self.smooth.config(command=self.smoothFunction)

        # the 3 scale widgets
        self.scaleRED = tk.Scale(self.frame3, from_=-1, to_=1, orient='vertical', activebackground='red', label='Red')
        self.scaleRED.grid(row=0, column=6, padx=10, rowspan=3)

        self.scaleGREEN = tk.Scale(self.frame3, from_=-1, to_=1, orient='vertical', activebackground='green',
                                   label='Green')
        self.scaleGREEN.grid(row=0, column=7, padx=10, rowspan=3)

        self.scaleBLUE = tk.Scale(self.frame3, from_=-1, to_=1, orient='vertical', activebackground='blue',
                                  label='Blue')
        self.scaleBLUE.grid(row=0, column=8, padx=10, rowspan=3)

        # ====================FRAME 4==========================
        self.displayStamp_Label = tk.Label(self.frame4, relief=tk.GROOVE)
        self.displayStamp_Label.configure(width=200, height=150, image=self.pic)
        self.displayStamp_Label.grid(padx=5, pady=5)

        self.addStamp_Button = tk.Button(self.frame4, text="Add Logo", command=self.loadStampPic)
        self.addStamp_Button.grid(sticky='S',pady=15)

        # ====================FRAME 5==========================
        self.processButton = tk.Button(self.frame5, text='Proceed', font='Arial 9 bold', command=self.manipulate)
        self.processButton.pack(side="right")

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
            self.photosList.append(Photo(j))  # Photo object that contain an image file and

        # Create buttons list displaying all images
        self.photo_button_List.clear()

        # Create Photo Button
        for i in range(len(self.photosList)):
            self.photo_button_List.append(tk.Button(self.frame1, image=self.photosList[i].thumbnailForButton))
            self.photo_button_List[i].configure(width=100, height=100, relief=tk.FLAT, bd=0)
            self.photo_button_List[i].grid(row=i // 5, column=i % 5 + 1, padx=5, pady=5)

            # Displaying different object by passing parameters to a function
            # Citation:
            self.photo_button_List[i].configure(command=lambda x=self.photosList[i].thumbnailForDisplay: self.display(x))

    def display(self, photo):
        self.display_Label.configure(image=photo, width=200, height=photo.height())
        self.display_Label.grid(row=0, column=0, padx=5, pady=10, sticky='swen')

    def blurFunction(self):
        self.manipulation['filter']='Blur'

    def contourFunction(self):
        self.manipulation['filter']='Contour'

    def edgeEnhanceFunction(self):
        self.manipulation['filter'] = 'Edge Enhance'

    def embossFunction(self):
        self.manipulation['filter'] = 'Emboss'

    def sharpenFunction(self):
        self.manipulation['filter'] = 'Sharpen'

    def smoothFunction(self):
        self.manipulation['filter'] = 'Smooth'


    def loadStampPic(self):
        file = filedialog.askopenfilename(filetypes=[("PNG files", "*.png"), ("JPG files", "*.jpg")])

        if file != '':
            self.stampPic = Photo(file)
            self.manipulation["stamp"] = self.stampPic.image
            self.stampPic.stamp = self.stampPic.createThumbnail(200)
            self.displayStamp_Label.configure(image=self.stampPic.stamp)

            # TO Update thumbnail for button in frame 2

            # for i in range(len(self.photosList)):
            #     self.photosList[i].thumbnailForButton = stampForView(self.photosList[i].thumbnailForButton, 0.2,
            #                                                          self.stampPic.image)
            #     self.photosList[i].thumbnailForDisplay = stampForView(self.photosList[i].thumbnailForDisplay, 0.2,
            #                                                           self.stampPic.image)

        else:
            pass


    def manipulate(self):
        if self.manipulation["filter"] == 'Blur':
            for pic in self.photosList:
                # TODO: code for applying filter
                self.processPhoto_list.append(stampForReal(pic.image.filter(ImageFilter.BLUR), 0.2, self.stampPic.image))

        elif self.manipulation['filter'] == 'Contour':
            for pic in self.photosList:
                self.processPhoto_list.append(stampForReal(pic.image.filter(ImageFilter.CONTOUR), 0.2, self.stampPic.image))

        elif self.manipulation['filter'] == 'Edge Enhance':
            for pic in self.photosList:
                self.processPhoto_list.append(stampForReal(pic.image.filter(ImageFilter.EDGE_ENHANCE), 0.2, self.stampPic.image))

        elif self.manipulation['filter'] == 'Emboss':
            for pic in self.photosList:
                self.processPhoto_list.append(stampForReal(pic.image.filter(ImageFilter.EMBOSS), 0.2, self.stampPic.image))

        elif self.manipulation['filter'] == 'Sharpen':
            for pic in self.photosList:
                self.processPhoto_list.append(stampForReal(pic.image.filter(ImageFilter.SHARPEN), 0.2, self.stampPic.image))

        elif self.manipulation['filter'] == 'Smooth':
            for pic in self.photosList:
                self.processPhoto_list.append(stampForReal(pic.image.filter(ImageFilter.SMOOTH), 0.2, self.stampPic.image))

        else:
            for pic in self.photosList:
                self.processPhoto_list.append(stampForReal(pic.image,0.2,self.stampPic.image))


        # elif self.manipulation['colorWeight'] !='':
        #     for pic in self.photosList:
        #         # TODO: code for manipulating color
        #         pass


        self.saveProject(self.processPhoto_list)
        self.processPhoto_list.clear()

    def saveProject(self, items_List):
        """
        This function will take a list of Images and save to disk. This function includes
            + asking for project name
            + Creating new folder
            + saving items
        :param items_List: <List> a list of Images
        :return: <void>
        """

        # Asking dialogue for the folder name
        inputProjectName = simpledialog.askstring("Input Project Name", "How do you like to name your project?",
                                                  parent=self.mainWin)

        # Prompt to choose location
        folderPath = filedialog.askdirectory() + '\{}'.format(inputProjectName)

        # Make a new folder "name"
        try:
            os.mkdir(folderPath)
            cnt = 0
            for item in items_List:
                cnt += 1
                item.save(folderPath + "\{}.jpg".format(cnt))

                # Ask of the users want to view the folder
            viewFolder = messagebox.askyesno("Save Completed!",
                                             "Your data has been saved to \{}. Do you want to view the folder?"
                                             .format(folderPath))
            # View newly created Folder
            if viewFolder:
                os.startfile(folderPath)

        except FileExistsError:
            # Error message
            ans = messagebox.askyesno("Folder Already Exists",
                                      "The Folder you are trying to created already exist. Do you want to continue?")
            if ans == 'no':
                print('no')
                pass
            else:
                self.saveProject(items_List)

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
