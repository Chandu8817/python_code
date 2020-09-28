# def add(x,y):
#     return x+y

# def show():
#     print(add(4,6))

# print(show())



# n1=int(input("no1 "))
# n2=int(input("no2 "))
# t1=n1
# t2=n2
# sum1=0
# sum2=0

# for i in range(n1):
#     r=n1%10
    
#     sum1=sum1+r
#     n1=n1//10


# for j in range(n2):
#     r=n2%10
#     sum2=sum2+r
#     n2=n2//10

    

# if sum1==sum2:
#     print('sum',t1+t2)
# else:
#     print("mul",t1*t2)


# for i in range(12,20):
#     print(i**2)

# s=0
# for j in range(0,11):
#     s=s+j

# print(s)

# r=""
# for i in range(0,7):
    
#     for j in range(0,7):
#         if (((j==1 or j==5) and i!=0) or  ((i==0 or i==3) and (j>1 and j<5))):

#             r=r+'*'
            
#         else:
#             r=r+" "
        
#     r=r+'\n'

# print(r)


# k=1
# for i in range(1,6):
#     print("\n")
#     for j in range(1,i+1):
    
#         print(k,end=',')

#         k=k+1


a=0
b=1
c=a+b
print(a,b)

for i in range(6-1):
    print(c,end=",")
    a=b
    b=c
    c=a+b
print('\n',c)