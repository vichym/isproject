from PIL import Image
import os


def createThumbnails(pic, w, h):
    newPic = pic.copy()
    newPic.thumbnail((w, h))
    return newPic


# def ThumnailsFolder():
#     path = r'C:\Users\LYHENG-HD\PycharmProjects\isp'
#     newpath = createNewFolder("Thumbnails", path)
#     for file in os.listdir('Images'):
#         thumnail = Image.open("Images\{}".format(file))
#         createThumbnails(thumnail, 220, 300).save(newpath + '\{}_{}'.format('thumbnail', file))


def createNewProjectFolder(name, path):
    """
    Creates new folder for a new project where final project is store.
    :param name: <string> the name of the new folder.
    :param path: <string> directory path
    :return: void
    """
    newPath = path + '\{}'.format(name)
    if not os.path.exists(newPath):
        os.mkdir(newPath)
    return newPath

class Picture:

    def __init__(self, *args):
        self.image = Image.open(args[0])
        self.thumList = {}
        self.thumVersion = self.createThumbnail(250, 300)

    def createThumbnail(self, w, h):
        name = (w, h)
        newPic = self.image.copy()
        newPic.thumbnail((w, h))
        self.thumList[name] = newPic
        return newPic

    def getThumlist(self):
        return self.thumList


if __name__ == '__main__':
    path = r'C:\Users\LYHENG-HD\PycharmProjects\isp\Images\wooster1.jpg'

