n=int(input("enter no"))
a=0
b=1
c=a+b
# print(a,b,c)
for i in range(n):
    a=b
    b=c
    c=a+b
    print(c)