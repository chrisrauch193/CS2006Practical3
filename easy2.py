ea = df[df["Economic Activity"].isin(range(0, 5))]

easy21 = pd.crosstab(index = (ea)['Region'], columns = 'count')
easy21

easy22 = pd.crosstab(index = (ea)['Age'], columns = 'count')
easy22
