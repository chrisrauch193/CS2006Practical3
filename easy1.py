easy12 = df.groupby(['Occupation','Approximated Social Grade']).count()
easy12

easy11 = df.groupby(['Region','Industry']).count()
easy11

easy12 = pd.crosstab(df['Occupation'], df['Approximated Social Grade'])
easy11 = pd.crosstab(df['Region'], df['Industry']) 
