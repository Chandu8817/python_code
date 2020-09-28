def convertcase():

    s=input("enter a str \n  ")
    l=[]
    for i in s:

        if i>='a' and i<='z':
            l.append(i.upper())
        elif i>='A' and i<='Z':
            l.append(i.lower())
        else:
            l.append(i)
    sc=''

    for i in l:
        sc=sc+i
        

    print(sc)


convertcase()


