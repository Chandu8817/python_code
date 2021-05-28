# qus35

# for i in range (5):
#     print("code better")

# i=1
# while i<=5:
#     print(i,"code better")

#     i+=1

# # qus36
# i=1
# while i<=10:
#     print(i,end=',')


#     i=i+1


# qus =37

# n=int(input("enter a no "))
# t=n

# while n>1:
#     print(t,end='*')
    
#     n=n-1
#     print(n,end=',')
#     t=t*n
# print("factorial is ",t)

# qus=38

# for i in range (1,11):
#     print(i**2)


# qus=39
# n=int(input("no "))

# i=1
# while i<=10:
#     print("{} X {} = {}".format(n,i,n*i))

#     i=i+1


# qus=40
# n=int(input("no "))
# rev=0
# while n>0:
#     r=n%10
#     rev=rev*10+r
#     n=n//10

# print(rev)

# qus=41

# n=int(input("no "))
# temp=n
# rev=0
# for i in range(n,0,-1):
    
#     r=n%10
#     rev=rev*10+r
#     n=n//10
#     if n==0:
#         break
# if rev==temp:
#     print(rev," is palindrom")
# else:
#     print(rev," is not a palindrom")

# qus=42


# n=int(input("no "))
# # vaid for 3 and 4 digit
# temp=n
# arm=0
# armf=0
# for i in range(n,0,-1):
    
#     r=n%10
#     arm=arm+r**3
#     armf=armf+r**4
#     n=n//10
#     if n==0:
#         break
# if arm==temp:
#     print(temp," is armstrong")
# elif armf==temp:
#     print(temp," is a armstrong")
# else:
#     print(temp," is not a armstrong")


# qus=43
# n=int(input("enter a num "))

# i=1
# print("factor of ",n, "is ")
# while i<n:
#     if n%i==0:
#         print(i)
#     i+=1


# qus=44

n=int(input("enter a num "))

i=1
sum=0
temp=n
print("factor of ",n, "is ")
while i<n:
    if n%i==0:
        sum=sum+i
        
    i+=1

if sum==temp:
    print(temp," is perfect number")
else:
    print(temp," is not perfect number")


# qus=45
# n=int(input("enter no "))
# a=0
# b=1
# c=a+b
# print(a,b)
# i=1
# while i<n:
#     a=b
#     b=c
#     print(c,end=' ')
#     c=a+b
#     # print(c,end=' ')

#     i=i+1

# qus=46

# n=int(input("no "))

# sum=0
# for i in range(n,0,-1):
#     r=n%10

#     sum=sum+r
#     n=n//10
#     if n==0:
#         break

# print(sum)

# qus=47

# n=int(input("no "))
# sum=0
# for i in range(1,n+1):
#     i=i**2
    
#     sum=sum+i

# print(sum)

# qus=48


# n=int(input("no "))
# even=0
# odd=0
# for i in range(0,n+1):
#     if i%2==0:
#         even=even+1
        
#     else:
#         odd=odd+1
        

# print('even no are ',even)
# print("odd no are ",odd)

# qus=49
# n1=int(input("no1 "))
# n2=int(input("no2 "))

# if n1>n2:
#     gr=n1
# else:
#     gr=n2
    
#     while True:
#         if gr%n1==0 and gr%n2==0:
#             lcm=gr
#             break

#         gr=gr+1

# print(lcm)


# qus=50

# n1=int(input("no1 "))
# n2=int(input("no2 "))

# if n1<n2:
#     sm=n1
# else:
#     sm=n2

# i=1
# while i<sm:
#     if n1%i==0 and n2%i==0:
#         hcf=i
      
#     i=i+1

# print(" the hfc of two no is ",hcf)
            


# qus=51

# n=int(input("no "))
# count=0
# i=1
# while i<=n:
#     if n%i==0:
#         count=count+1
        
    
#     i=i+1
# if count==2:
#     print("prime")
# else:
#     print("not a prime")

# qus=52 


# s=0
# for i in range (1,8):
#     if (i%2!=0):
#         x=i+1
#         s=i-x+s
#         print("{}-{}+".format(i,x),end='')    
# print("=",s)



# qus=52-2nd

# n=int(input("enter no "))
# sum=0
# i=1
# while i<=n:
#     j=i
#     t=j 
#     while j>1:
#         j=j-1
#         t=t*j
#     if t!=0:
#         a={t}
#         li=list(a)
#         # print(li)
#         l=len(li)


#         for k in range(l):
#             sum=sum+li[k]
            
#             # print("{} ".format(li[k]),end='')

        
#     i=i+1

# for i in range(1,n+1):
#     print(i,end="!+")
# print("=",sum)


# qus=53

# i=1
# while i<=5:
#     print("\n")
#     j=1
#     while j<=5:
#         print("*",end='')
#         j=j+1
#     i=i+1

# qus=53-2nd

# i=1
# while i<=5:
#     print("\n")

#     j=1
#     while j<=i:
#         print("*",end='')

#         j=j+1
#     i=i+1

# qus=53 3rd

# i=5
# while i>=1:
#     print("\n")

#     j=5
#     while j>=i:
#         print(j,end='')

#         j=j-1
#     i=i-1


# qus=53 4th

# i=1
# while i<=5:
#     print("\n")

#     j=1
#     while j<=i:
#         print(j,end='')

#         j=j+1
#     i=i+1


# i=65
# while i<=69:
#     print("\n")
#     j=65
#     while j<=i:
#         print(chr(j),end="")

#         j=j+1
#     i=i+1

# qus=54

# n=int(input("enter no "))

# i=1


# while i<=100:

#     j=i
#     c=0
#     while j>=1:

#         if i%j==0:
#             c=c+1
        
#         j=j-1
#     if c==2:
#         print(i,end=',')


#     i=i+1

# qus=55

# i=1

# while i<1000:


#     j=i
#     t=j
#     s=0
#     while j>0:
#         r=j%10
#         s=s+r**3
#         j=j//10
#     if s==t:
#         print(s)

#     i=i+1


# qus=56 

# def rept(n):

#     print("code better ")

#     if n==1:
#         return 1
#     else:
#         return n*rept(n-1)

# rept(5)


# # qus=57

# print("factorial of given no is ")
# def fact(n):
    
#     if n==0:
#         return 0

#     elif n==1:
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(5))
