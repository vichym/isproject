'''This is the file the user run to use the ISP program'''

#-------import------------------
import os
import tkinter as tk
from tkinter import simpledialog, messagebox

from PIL import ImageFilter

from main_window_backEnd import *

class Window:
    def __init__(self):
        '''The window of the ISP program. Create the main window, the variables used throughout the program, the window's frames and widgets.'''
        self.processPhoto_list = []     # This will be list holding the final result
        self.photosList = []            # This is the list holding the pictures the user will choose
        self.stampPic = None            # This variable holds the stamp picture
        self.mainWin = tk.Tk()          # The main window
        self.manipulation = {"filter": '', "stamp": {}}    # This will hold what the user change to the pictures

# -------The user interface--------------------------------
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
        pic = Image.open('download.jpg')
        self.pic = ImageTk.PhotoImage(pic)

        self.blurPic = ImageTk.PhotoImage(pic.filter(ImageFilter.BLUR))
        self.blur = tk.Button(self.frame3, image=self.blurPic, width=90, height=90, text='Blur',compound='center')
        self.blur.grid(row=0, column=0, padx=5, pady=5)
        self.blur.config(command=self.blurFunction)

        self.contourPic = ImageTk.PhotoImage(pic.filter(ImageFilter.CONTOUR))
        self.contour = tk.Button(self.frame3, image=self.contourPic, width=90, height=90, text='Contour', compound='center')
        self.contour.grid(row=0, column=1, padx=5, pady=5)
        self.contour.config(command=self.contourFunction)

        self.edgeEnhancePic = ImageTk.PhotoImage(pic.filter(ImageFilter.EDGE_ENHANCE))
        self.edgeEnhance = tk.Button(self.frame3, image=self.edgeEnhancePic, width=90, height=90, text='Edge Enhance', compound='center')
        self.edgeEnhance.grid(row=0, column=2, padx=5, pady=5)
        self.edgeEnhance.config(command=self.edgeEnhanceFunction)

        self.embossPic = ImageTk.PhotoImage(pic.filter(ImageFilter.EMBOSS))
        self.emboss = tk.Button(self.frame3, image=self.embossPic, width=90, height=90, text = 'Emboss', compound='center')
        self.emboss.grid(row=1, column=0, padx=5, pady=5)
        self.emboss.config(command=self.embossFunction)

        self.sharpenPic = ImageTk.PhotoImage(pic.filter(ImageFilter.SHARPEN))
        self.sharpen = tk.Button(self.frame3, image=self.sharpenPic, width=90, height=90, text='Sharpen', compound='center')
        self.sharpen.grid(row=1, column=1, padx=5, pady=5)
        self.sharpen.config(command=self.sharpenFunction)

        self.smoothPic = ImageTk.PhotoImage(pic.filter(ImageFilter.SMOOTH))
        self.smooth = tk.Button(self.frame3, image=self.smoothPic, width=90, height=90, text='Smooth',compound='center')
        self.smooth.grid(row=1, column=2, padx=5, pady=5)
        self.smooth.config(command=self.smoothFunction)

        self.cancelFilter = tk.Button(self.frame3, text='Cancel filter effect')
        self.cancelFilter.grid(row=0,column=3)
        self.cancelFilter.config(command=self.cancelFilterFunction)

        # ====================FRAME 4==========================
        self.displayStamp_Label = tk.Label(self.frame4, relief=tk.GROOVE,text='Your stamp will be displayed here')
        self.displayStamp_Label.grid(padx=5, pady=5)

        self.addStamp_Button = tk.Button(self.frame4, text="Add Stamp", command=self.loadStampPic)
        self.addStamp_Button.grid(sticky='S',pady=15)

        # ====================FRAME 5==========================
        self.processButton = tk.Button(self.frame5, text='Proceed', font='Arial 9 bold', command=self.manipulate)
        self.processButton.pack(side="right")

#------------------------The functions---------------------------------------------------------------------------
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
        '''Display the original picture to Frame 2'''
        self.display_Label.configure(image=photo, width=200, height=photo.height())
        self.display_Label.grid(row=0, column=0, padx=5, pady=10, sticky='swen')

    def blurFunction(self):
        '''Remember that the user chose the Blur button'''
        self.manipulation['filter']='Blur'

    def contourFunction(self):
        '''Remember that the user chose the Contour button'''
        self.manipulation['filter']='Contour'

    def edgeEnhanceFunction(self):
        '''Remember that the user chose the Edge Enhance button'''
        self.manipulation['filter'] = 'Edge Enhance'

    def embossFunction(self):
        '''Remember that the user chose the Emboss button'''
        self.manipulation['filter'] = 'Emboss'

    def sharpenFunction(self):
        '''Remember that the user chose the Sharpen button'''
        self.manipulation['filter'] = 'Sharpen'

    def smoothFunction(self):
        '''Remember that the user chose the Smooth button'''
        self.manipulation['filter'] = 'Smooth'

    def cancelFilterFunction(self):
        '''Delete all the filters the user chose'''
        self.manipulation['filter'] = ''

    def loadStampPic(self):
        '''SHow the stamp picture the user chose'''
        file = filedialog.askopenfilename(filetypes=[("PNG files", "*.png"), ("JPG files", "*.jpg")])

        if file != '':
            self.stampPic = Photo(file)
            self.manipulation["stamp"] = self.stampPic.image
            self.stampPic.stamp = self.stampPic.createThumbnail(200)
            self.displayStamp_Label.configure(image=self.stampPic.stamp)

        else:        #If the user press cancel or X
            pass     # Stop (because the user choose cancel/ press X)


    def manipulate(self):
        '''Change the pcitures according to the filters, stamp chosen
        and save the results to a file and view the file'''
        if self.displayStamp_Label['image'] == '':   # There is no stamp chosen
            if self.manipulation["filter"] == 'Blur':
                for pic in self.photosList:
                    self.processPhoto_list.append(pic.image.filter(ImageFilter.BLUR))

            elif self.manipulation['filter'] == 'Contour':
                for pic in self.photosList:
                    self.processPhoto_list.append(pic.image.filter(ImageFilter.CONTOUR))

            elif self.manipulation['filter'] == 'Edge Enhance':
                for pic in self.photosList:
                    self.processPhoto_list.append(pic.image.filter(ImageFilter.EDGE_ENHANCE))

            elif self.manipulation['filter'] == 'Emboss':
                for pic in self.photosList:
                    self.processPhoto_list.append(pic.image.filter(ImageFilter.EMBOSS))

            elif self.manipulation['filter'] == 'Sharpen':
                for pic in self.photosList:
                    self.processPhoto_list.append(pic.image.filter(ImageFilter.SHARPEN))

            elif self.manipulation['filter'] == 'Smooth':
                for pic in self.photosList:
                    self.processPhoto_list.append(pic.image.filter(ImageFilter.SMOOTH))
            elif self.manipulation['filter'] == '':
                for pic in self.photosList:
                    self.processPhoto_list.append(pic.image)

        else:                  # if there is a stamp chosen
            if self.manipulation["filter"] == 'Blur':
                for pic in self.photosList:
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

            else:      # If there was no filter chosen
                for pic in self.photosList:
                    self.processPhoto_list.append(stampForReal(pic.image,0.2,self.stampPic.image))

        self.saveProject(self.processPhoto_list)  # Save the result
        self.processPhoto_list.clear()      # Delete the saving list so that the next product starts afresh
        self.manipulation['filter'] = ''    # Delete the filter so that the next product starts afresh

    def saveProject(self, items_List):   # Can only run in PC.
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
        if inputProjectName == None:
            pass
        else:
            # Prompt to choose location
            a = filedialog.askdirectory()
            folderPath = a + '\{}'.format(inputProjectName)

            if a == "":
                pass
            else:
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
                    print('viewFolder=',type(viewFolder),viewFolder)
                    # View newly created Folder
                    if viewFolder:
                        os.startfile(folderPath)
                    else:
                        pass

                except FileExistsError:
                    # Error message
                    ans = messagebox.askyesno("Folder Already Exists",
                                              "The Folder you are trying to created already exist. Do you want to continue?")

                    if ans is False:
                        pass
                    else:
                        self.saveProject(items_List)
# ------------------RUN------------------------------------

    def run(self):
        ''''''
        self.mainWin.mainloop()

#--------------------TEST----------------------------------
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
    # We tested 4 cases: 1) with filter and stamp, 2) without filter and with stamp, 3) without stamp and with filter, 4) without filter and stamp

