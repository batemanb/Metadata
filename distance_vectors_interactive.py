import pandas
import readmetaData

# create a dataframe from an excel file
df = pandas.read_excel('C:/Users/batemanb/Documents/Mizzou_UGR/SEM images/20210607/20210607.xlsx')
image1 = int(input("Enter number for first image"))
image2 = int(input("Enter number for second image"))
print(readmetaData.find_differences_pandas(df, image1, image2))
