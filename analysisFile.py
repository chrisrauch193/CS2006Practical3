import pandas as pd

def basic21(df):
    #Basic Requirement 2.1
    return "The number of records is " + str(len(df))

def basic22(df):
    #Basic Requirement 2.2
    return "All Data Types:\n" + str(df.dtypes)

def basic23(df)
    retString = ""
    #Basic Requirement 2.3
    for column in df:
        if (column != "Person ID"):
            retString = retString + (str(column)+ " Counts\n" +str(df[column].value_counts()) + "\n")
# import matplotlib as mpl
# pd.Series.__unicode__ = pd.Series.to_string
#
# df=pd.read_csv("./census2011.csv")
# df
# len(df)
# print("All Data Types:\n" + str(df.dtypes))
# print("number of records = " + str(df['Person ID'].count()))
# df['Residence Type'].value_counts()
#
# for column in df:
#     if (column != "Person ID"):
#         print(str(column)+ " Counts\n" +str(df[column].value_counts()) + "\n")
#
# print(str(df.groupby('Economic Activity')))
#
# newdf = df
# newdf
#
# #for index, row in newdf.iterrows():
#  #   newdf.set_value('Residence Type', index, 10)
#     #print(str(row['Residence Type']))
# #newdf
# newdf.loc[0,'Residence Type'] = 10
#
# newdf
#
# for column in newdf:
#     print(column)
#
# for index, row in newdf.iterrows():
#     #print(str(row))
#
# row = 0
# column = 'Residence Type'
# df.loc[row,column] = 10
# df
