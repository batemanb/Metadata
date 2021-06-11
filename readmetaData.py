# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 12:41:49 2021

@author: batemanb
"""

import exifread  # used to interact with tags in tif files
from pathlib import Path  # a class based module for interacting with files


def get_coordinates(directory, filetype):
    '''
    Creates a list of x,y coordinates found in the metadata of tif files.

    Parameters
    ----------
    directory : TYPE String
        DESCRIPTION. A directory path
    filetype : TYPE String
        DESCRIPTION. A file extension

    Returns
    -------
    list_x : TYPE List
        DESCRIPTION. A list of x values from metadata of EMC imaging
    list_y : TYPE List
        DESCRIPTION. A list of y values from metadata of EMC imaging

    '''
    # make an array of objects corresponding to all the tif files in a directory
    paths = Path(directory).glob('**/*.tif')

    # I use these lists to store the (x,y) coordinate pairs
    list_x = []
    list_y = []
    for path in paths:  # iterate over every file in paths
        path_in_str = str(path)  # get a string corresponding to the current path
        f = open(path_in_str, 'rb')  # open that file in read binary

        # Return Exif tags
        tags = exifread.process_file(f)

        # Print the tag/ value pairs
        for tag in tags.keys():
            if tag in ('Image Tag 0x877A'):
                # print("Key: %s, value %s" % (tag, tags[tag]))
                test_string = tags[tag]
                x = float(test_string.printable.split("StageX=")[1].split("\r")[0])
                y = float(test_string.printable.split("StageY=")[1].split("\r")[0])
                list_x.append(x)
                list_y.append(y)
        f.close()
    return list_x, list_y


def find_differences(list_x, list_y):
    delx = []
    dely = []
    for i in range(len(list_x)):
        # each item in delta lists is the difference between the ith item in the
        # x,y lists and the previous (i-1). This provides vector components that
        # point from the i-1 image to the ith image. Note the first delta value
        # points from the last file in the list to the first.
        delx.append(list_x[i] - list_x[i - 1])
        dely.append(list_y[i] - list_y[i - 1])
    return delx, dely


def main():
    x, y = get_coordinates('C:/Users/batemanb/SpyderProjects/metaDataDifferenceCalc', '**/*.tif')
    delx, dely = find_differences(x, y)
    print("X Coordinates = {0} \nY Coordinates = {1}".format(x, y))
    print("delta x = {0} \ndelta y = {1}".format(delx, dely))


main()