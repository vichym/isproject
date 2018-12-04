from PIL import Image
import os
from tkinter import filedialog
from main_window_gui import *


class Project:

    def __int__(self):
        self.window = Window2.__init__()
        self.list = selectFilesDialogue(self.window)
        self.name = Window2.getProjectName()
        self.path = ''
        self.rootFolder = createNewProjectFolder(self.name, self.path)

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName



class Picture:
    """
    Picture objects contain a full size image object and a list of different size thumbnails.
    """

    def __init__(self, *args):
        self.image = Image.open(args[0])
        self.thumbnailsList = {}
        self.thumbnailVersion = self.createThumbnail(250, 300)

    def createThumbnail(self, w, h):
        name = (w, h)
        newPic = self.image.copy()
        newPic.thumbnail((w, h))
        self.thumbnailsList[name] = newPic
        return newPic

    def getThumlist(self):
        return self.thumbnailsList


def createThumbnails(pic, w, h):
    """
    Create a thumnails with specified width and height of a picture.
        :param pic: (Image)
        :param w: (int)
        :param h: (int)
        :return: (Thumnail)
    """
    newPic = pic.copy()
    newPic.thumbnail((w, h))
    return newPic


def createNewProjectFolder(name, path):
    """
    Creates new folder for a new project where final project is store if there is no project folder exist
        :param name: <string> the name of the new folder.
        :param path: <string> directory path
        :return: void
    """
    newPath = path + '\{}'.format(name)
    if not os.path.exists(newPath):
        os.mkdir(newPath)
    return newPath


def selectFilesDialogue(rootWindow):
    """
    create a dialogue window to prompt the users to selects image files to process.
        :param rootWindow: (window) the root window
        :return: (list) list of the path to the selected files
    """
    files = filedialog.askopenfilenames(parent=rootWindow, title='Choose a file')
    selectedFiles = rootWindow.tk.splitlist(files)
    return selectedFiles
