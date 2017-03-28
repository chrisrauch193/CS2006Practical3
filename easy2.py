import pandas as pd

def easy21(df):
    #Filtering the Dataset to be economic code from 1-4
    ea = df[df["Economic Activity"].isin(range(1, 5))]
    # Easy 2 Part 1 using CrossTab
    easy21 = pd.crosstab(index = (ea)['Region'], columns = 'count')
    return str(easy21)

def easy22(df):
    #Filtering the Dataset to be economic code from 1-4
    ea = df[df["Economic Activity"].isin(range(1, 5))]
    # Easy 2 Part 2 using CrossTab
    easy22 = pd.crosstab(index = (ea)['Age'], columns = 'count')
    return str(easy22)
