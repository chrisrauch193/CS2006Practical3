a = [(1,1),(1,2),(1,3),(1,4),(1,5)]


for i in range(0,len(a)):
    b = a[:i] + a[i+1:]
    print(b)
