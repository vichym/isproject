from tkinter import filedialog

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

def stampForView(image, ratio, stampPNG):
    """
    This function resize the stampPNG to the specify ratio to the target image and stamp.
    :param image: Target Image
    :param ratio: 0<ratio<1
    :param stampPNG: PNG image that have transparent background
    :return: Image
    """

    w, h = image.size
    lw = w * ratio
    lh = h * ratio
    photo = image.copy()
    stampPNG.thumbnail((lw, lh), Image.ANTIALIAS)
    photo.paste(stampPNG, (int(w - w * ratio - lw), int(h - ratio * h)), stampPNG)
    photo = ImageTk.PhotoImage(photo)
    return photo


def stampForReal(image, ratio, stampPNG):
    """
    This function resize the stampPNG to the specify ratio to the target image and stamp.
    :param image: Target Image
    :param ratio: 0<ratio<1
    :param stampPNG: PNG image that have transparent background
    :return: Image
    """

    w, h = image.size
    lw = w * ratio
    lh = h * ratio
    photo = image.copy()
    stampPNG.thumbnail((lw, lh), Image.ANTIALIAS)
    photo.paste(stampPNG, (int(w - w * ratio - lw), int(h - ratio * h)), stampPNG)
    return photo

def manipulate(dict, photoList):
    if dict["filter"] is not None:
        for pic in photoList:
            # TODO: code for applying filter
            pass
    elif dict['stamp'] is not None:
        for pic in photoList:
            # TODO: code for applying stamp
            pass
    elif dict['colorWeight'] is not None:
        for pic in photoList:
            # TODO: code for manipulating color
            pass


def Test(ratio):
    photo0 = Image.open("astilbe.jpg")
    w, h = photo0.size
    lw = w * ratio
    lh = h * ratio
    photo = photo0.copy()
    photo.show()
    watermark = Image.open("ll.png").copy()
    watermark.show()

    watermark.thumbnail((lw, lh), Image.ANTIALIAS)

    photo.paste(watermark, (int(w - w * ratio - lw), int(h - ratio * h)), watermark)
    photo.show()


if __name__ == '__main__':
    # mainWin = tk.Tk()
    # mainWin.withdraw()
    # list = []
    # saveProject(list)
    # mainWin.mainloop()

    # Test(0.1)

    files = filedialog.askopenfilename(title='Choose a file')
    Image.open(files).show()
