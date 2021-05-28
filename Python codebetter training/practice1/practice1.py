# print(''' codebetter\n"codebetter"\n'codebetter' ''')
# print( 3*'*','\n',5*'*')
# n=5
# print(n**2)
# radius=6
# print('area of circle', 3.14*radius)
# p=200000
# t=2
# r=12.5
# si=p*r*t/100
# print('simple interest of',p,' is ', si)


# basic_anyally=200000
# da=basic_anyally*10/100
# ta=basic_anyally*12/100
# gs=basic_anyally+da+ta
# print("the gross slary is ", gs)

# P=67
# C=87
# M=90
# H=98
# E=88
# total=P+C+M+H+E
# print(total)
# per=total*100/500
# print(per)

# a=10
# b=20
# a,b=b,a
# print("a",a, 'b',b)
# a=10
# b=30
# c=a
# a=b
# b=c
# print('a',a,'b',b)

# s=input("enter charcter")
# n=int(input('num '))
# print(ord(s),chr(n))

# n=int(input('num '))
# s=0
# r=n%10
# s=s+r
# n=n//10
# r=n%10
# s=s+r
# n=n//10
# r=n%10
# s=s+r
# print(s)

# n1=120
# n2=345
# n3=456
# print((n1+n2+n3)/3)


# n=3456
# rv=0
# r=n%10
# rv=rv*10+r
# n=n//10
# r=n%10
# rv=rv*10+r
# n=n//10
# r=n%10
# rv=rv*10+r
# n=n//10
# r=n%10
# rv=rv*10+r
# print(rv)

# amt=4567
# twothousand=2000
# list=[500,200,100,50,20,10,5,2,1]

# c=amt//twothousand
# if c!=0:
#     print(twothousand, c)
# amt=amt-c*twothousand
# c=amt//list[1]
# if c!=0:
#     print(list[1], c)
# amt=amt-c*list[1]
# c=amt//list[2]
# if c!=0:
#     print(list[2], c)
# amt=amt-c*list[2]
# c=amt//list[3]
# if c!=0:
#     print(list[3], c)
# amt=amt-c*list[3]

# c=amt//list[4]
# if c!=0:
#     print(list[4], c)
# amt=amt-c*list[4]

# c=amt//list[5]
# if c!=0:
#     print(list[5], c)
# amt=amt-c*list[5]

# c=amt//list[6]
# if c!=0:
#     print(list[6], c)
# amt=amt-c*list[6]


# c=amt//list[7]
# if c!=0:
#     print(list[7], c)
# amt=amt-c*list[7]


# n1=int(input('num1 '))
# n2=int(input('num2 '))

# if n1%n2==0:
#     print('divisable')
# else:
#     print('not a divisable')

# n2=int(input('num2 '))
# if n2%2==0:
#     print('even')
# else:
#     print('odd')



# n1=int(input('num1 '))
# n2=int(input('num2 '))

# if n1>n2:
#     print(n1,'biger')
# elif n1==n2:
#     print(n1,n2,'same')
# else:
#     print(n2,'is biger')

# l=[2,3,3,3,3,3,4,4,4,4,4,4]
# d={}
# for i in l:
#     if i in d:
#         d[i] += 1
#         print(d[i])
#     else:
        
#         d[i] = 1
#         print(d[i])
        
# print(d)



# def reverse(n):
#     rv=0
#     while n>0:
#         r=n%10
#         rv=rv*10+r
#         n=n//10

#     print(rv)
# n=int(input("enter num "))
# reverse(n)

# class Bank:
#     branch="SBI Indore "

#     def __init__(self,name,acc_no):

#         self.name=name
#         self.acc_no=acc_no
        
#     def dispalyprofile(self):
#         print(self.name,"\n",self.acc_no)

# obj=Bank('chandu',12345)

# obj.dispalyprofile()


# i=1
# while i<=6:
#     print("\n")
#     k=6
#     while k>=i:
#         print(" ",end="")

#         k=k-1
#     j=1
#     while j<=i:
#         print("$",end='')

#         j=j+1
#     j=1
#     while j<i:
#         print("$",end='')

#         j=j+1
#     i=i+1

# i=1
# while i<=6:
#     print("\n")

#     k=1
#     while k<=i:
#         print(" ",end='')
#         k=k+1
#     j=i
#     while j<=6:
#         print(j,end='')

#         j=j+1
#     j=i
#     while j<6:
#         print(j,end='')

#         j=j+1
#     i=i+1


# i=6
# while i>=1:
#     print("\n")
#     j=1
#     while j<=i:
#         print(j,end='')

#         j=j+1
#     i=i-1



