try:
    n=int(input("enter num"))
    ns=str(n)
    l=[]
    l2=[]
    for i in ns:
        l.append(int(i))
except Exception as e:
    # print(e)
    print("negative not allowed")
else: 

    for i in l:

        if i>1:
            print("no")
            break

    else:
        print("bin")