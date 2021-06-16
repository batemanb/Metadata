import pandas
import readmetaData
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

# create a dataframe from an excel file
Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
df = pandas.read_excel(filename)
image1 = int(input("Enter number for first image"))
image2 = int(input("Enter number for second image"))
print(readmetaData.find_differences_pandas(df, image1, image2))
