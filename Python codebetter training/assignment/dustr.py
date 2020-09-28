s=input("str ")
l=[]
l2=[]
for i in s:
    if i not in l:
        l.append(i)
    elif i not in l2:
        l2.append(i)
print(l2)