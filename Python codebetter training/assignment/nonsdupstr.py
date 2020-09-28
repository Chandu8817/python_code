# s=input("enter str")
s='chandrashekhar'
l=[]
l2=[]
for i in s:
    if i not in l:
        l.append(i)
    elif i not in l2:
        l2.append(i)


for i in l2:
    if i in l:
        l.remove(i)

print(l)