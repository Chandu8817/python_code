s=int(input("enter the sum"))

a=[]
n=int(input("len of arry"))
for i in range(n):
    el=int(input("int el "))
    a.append(el)

print(a)
sa=[]
for i in range(len(a)):
    # print(a[i])
    
    for j in range(i+1,len(a)):

        if s==a[i]+a[j]:
            
            sa.append(a[i])
            sa.append(a[j])
        else:
            pass

print(sa)