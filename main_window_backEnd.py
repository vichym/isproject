import  tkinter as tk
from tkinter import filedialog


def selectFilesDialogue(rootWindow):
    """
    create a dialogue window to prompt the users to selects image files to process.
    :param rootWindow: (window) the root window
    :return: (list) list of the path to the selected files
    """

    filez = filedialog.askopenfilenames(parent=rootWindow,title='Choose a file')
    list = rootWindow.tk.splitlist(filez)
    print(list)
    return list



