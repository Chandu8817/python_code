s1=input("enter a string ")
s2=input("enter a string ")


sl1=[]
sl2=[]
for k in s1:
    sl2.append(k)
sl2.sort()


for i in s1:
    sl1.append(i)

sl1.sort()

if sl1==sl2:
    print("Anagram")
else:
    print("not")
print(sl1,sl2)


    
