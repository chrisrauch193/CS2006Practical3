#Easy Extension 1 part 1 Using crosstab
import pandas as pd

def easy11Crosstab(df):
    dfeasy11 = pd.crosstab(df['Region'], df['Industry'])
    return str(dfeasy11)

def easy12Crosstab(df):
    #Easy Extension 1 part 2 using crosstab
    dfeasy12 = pd.crosstab(df['Occupation'], df['Approximated Social Grade'])
    return str(dfeasy12)

def easy11GroupBy(df):
    #Easy 1 part 1 using GroupBy
    easy11 = df.groupby(['Region','Industry'])['Person ID'].count()
    easy11 = pd.Series.to_frame(easy11)
    easy11.columns.values[0] = 'Counts'
    return str(easy11)

def easy12GroupBy(df):
    #Easy 1 part 2 using GroupBy
    easy12 = df.groupby(['Occupation','Approximated Social Grade'])['Person ID'].count()
    easy12 = pd.Series.to_frame(easy12)
    easy12.columns.values[0] = 'Counts'
    return str(easy12)
