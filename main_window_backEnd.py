import os
from tkinter import filedialog, simpledialog, messagebox

from main_window_gui import *


class Photo:
    """
    Picture objects contain a full size image object and a list of different size thumbnails.
    """

    def __init__(self, *args):
        self.image = Image.open(args[0])
        self.thumbnailForButton = self.createThumbnail(100)
        self.thumbnailForDisplay = self.createThumbnail(200)

    def createThumbnail(self, maxSideLength):
        """
        Create a thumbnail that fits the maximum side length of maxSideLength
        :param maxSideLength: the maximum length of the container
        :return: Image
        """
        w, h = self.image.size

        if w > h:
            newW = maxSideLength
            newH = int(h * newW / w)
        elif w < h:
            newH = maxSideLength
            newW = int(w * newH / h)
        else:
            newW = maxSideLength
            newH = maxSideLength
        newPic = self.image.copy()
        newPic.thumbnail((newW, newH))
        # covert to ImageTK object to be used with tkinter button widget
        newPic = ImageTk.PhotoImage(newPic)
        return newPic


def selectFilesDialogue(rootWindow):
    """
    create a dialogue window to prompt the users to selects image files to process.
        :param rootWindow: (window) the root window
        :return: (list) list of the path to the selected files
    """
    files = filedialog.askopenfilenames(parent=rootWindow, title='Choose a file')
    selectedFiles = rootWindow.tk.splitlist(files)
    return selectedFiles


def saveProject(items_List, mainWin):
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
                                              parent=mainWin)

    # Prompt to choose location
    folderPath = filedialog.askdirectory() + '\{}'.format(inputProjectName)

    # Make a new folder "name"
    try:
        os.mkdir(folderPath)
    except FileExistsError:
        # Error message
        messagebox.showinfo("Folder Already Exists", "The Folder you are trying to created already exist")
        saveProject(items_List)

    # Save items in the list to the new folder
    for item in items_List:
        os.path.join(folderPath, item)

    # Ask of the users want to view the folder
    viewFolder = messagebox.askyesno("Save Completed!",
                                     "Your data has been saved to \{}. Do you want to view the folder?"
                                     .format(folderPath))
    # View newly created Folder
    if viewFolder:
        os.startfile(folderPath)


def stamp(ratio):
    photo0 = Image.open("astilbe.jpg")
    w, h = photo0.size
    lw = w * ratio
    lh = h * ratio
    photo = photo0.copy()
    watermark = Image.open("ll.png").copy()

    watermark.thumbnail((lw, lh), Image.ANTIALIAS)

    photo.paste(watermark, (int(w - w * ratio - lw), int(h - ratio * h)), watermark)
    photo.show()


if __name__ == '__main__':
    # mainWin = tk.Tk()
    # mainWin.withdraw()
    # list = []
    # saveProject(list)
    # mainWin.mainloop()

    stamp(0.1)
