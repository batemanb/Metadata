import exifread
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

# Open image file for reading (binary mode)


def get_coordinates(filename):

    # Return Exif tags
    file = open(filename, 'rb')
    tags = exifread.process_file(file)

    # Print the tag/ value pairs
    for tag in tags.keys():
        if tag in ('Image Tag 0x877A'):
            # print("Key: %s, value %s" % (tag, tags[tag]))
            test_string = tags[tag]
            x = float(test_string.printable.split("StageX=")[1].split("\r")[0])
            y = float(test_string.printable.split("StageY=")[1].split("\r")[0])
    file.close()
    return x, y


def main():
    Tk().withdraw()
    image1 = askopenfilename()
    image2 = askopenfilename()
    x1, y1 = get_coordinates(image1)
    x2, y2 = get_coordinates(image2)
    delx = x2 - x1
    dely = y2 - y1
    print("delta x = %f" % delx)
    print("delta y = %f" % dely)


if __name__ == '__main__':
    main()
