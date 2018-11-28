from PIL import Image
import os


def createThumbnails(pic, w, h):
    newPic = pic.copy()
    newPic.thumbnail((w, h))
    return newPic


# def BWFolder():
#     path = r'C:\Users\LYHENG-HD\PycharmProjects\isp'
#     newpath = createNewFolder("B&W", path)
#     for file in os.listdir('Images'):
#         newf = Image.open("Images\{}".format(str(file))).copy()
#         newf.convert(mode='L').save(newpath + '\{}_{}'.format("BW", file))


def ThumnailsFolder():
    path = r'C:\Users\LYHENG-HD\PycharmProjects\isp'
    newpath = createNewFolder("Thumbnails", path)
    for file in os.listdir('Images'):
        thumnail = Image.open("Images\{}".format(file))
        createThumbnails(thumnail, 220, 300).save(newpath + '\{}_{}'.format('thumbnail', file))


def createNewFolder(name, path):
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


if __name__ == '__main__':
    path = r'C:\Users\LYHENG-HD\PycharmProjects\isp\Images\wooster1.jpg'
    # createNewFolder("B&W", path)
    ThumnailsFolder()
