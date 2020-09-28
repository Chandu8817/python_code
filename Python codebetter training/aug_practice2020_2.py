# Q.1 Write a program to print given format using single print 

# print("code-better \n \"code-better\" \n \'code-better\' ")

# Q.2 Write a program to print given format using printf
# function. * 
# print( "*"*3,"\n","*"*5,"\n","*"*7)

# Q.3 square of a num

# num=int(input("num \n"))
# print(f"the square of {num} is ", num**2)

# Q.4 area of crcile
# radius=int(input("num \n"))

# pie=3.14
# print(f"the aresa of cricle is ", round(radius*pie,5))





# Q.5 simple interest 

# p=500000
# t=60
# r=11.25

# si=(p*r*t)/100
# print(si)


# Q.6 gross salary 

# ta=10000
# ba=(ta*15)/100
# da=(ta*25)/100

# gs=(ba+ta+ta)*12

# print(gs)


# Q.7 percent of marks

# p=int(input("enter marks of physics"))
# c=int(input("enter marks of chemistry "))
# m=int(input("enter marks of math"))
# e=int(input("enter marks of english"))
# h=int(input("enter marks of hindi"))
# total=(p+c+m+e+h)
# per=(total*100)/500
# print(total, " \n",per)



# a,b=20,30

# c=a
# a=b
# b=c
# print(f"the value of a ={a} and b={b} after swap ")

# a,b=30,40
# b,a=a,b
# print(f"the value of a ={a} and b={b} after swap ")


# Q.10 accept char output int

# char= input("enter a char /")

# print(ord(char))


# num=123
# s=0

# r=num%10
# s=s+r
# num=num//10
# r=num%10
# s=s+r
# num=num//10
# r=num%10
# s=s+r


# print(s)


# a,b,c=45,67,78
# av=(a+b+c)/3
# print(av)


# n=int(input("enter the num \n"))

# rv=0

# while n>0:

#     r=n%10
#     rv=rv*10+r
#     n=n//10

# print(rv)

# amt= int(input("enter amount"))

# list_of_currency= [2000,500,200,100,50,20,10,5,2,1]

# for i in list_of_currency:

#     c=amt//i
#     if c!=0:
#         print(i,":" ,c)
#     # amt=amt-c*i/
#     amt=amt%i

    


# --------------------------------
# Control flow (if - else)

# --------------------------------

# Q.16

# n1=int(input("num-1 \n"))
# n2=int(input("num-2"))

# if n1%n2==0:
#     print("num is divisible")
# else:
#     print("num is not divisible")

# n=int(input("num \n"))

# if n%2==0:
#     print("even")
# else:
#     print("odd")


# n1=int(input("num-1 \n"))
# n2=int(input("num-2"))

# if n1>n2:
#     print("num1 is bigger")
# else:
#     print("num2 is bigger")


# n1=int(input("num-1 \n"))
# n2=int(input("num-2 \n"))
# n3=int(input("num-3 \n"))

# if n1>n2 and n1>n3:
#     print("num1 is bigger")
# elif n2>n1 and n2>n3:
#     print("num2 is bigger")
# else:
#     print("num3 is bigger") 


# age= int(input("enter your age \n"))

# if age>=18:
#     print("he//she can vote ")
# else:
#     print("he//she c'ant vote")

# num= int(input("enter a number \n"))

# if num>0:
#     print("positive")
# elif num<0:
#     print("negative")
# else:
#     print("num is zero")

# num= int(input("enter a number \n"))

# t=num
# p=0
# while num>0:
#     r=num%10

#     p=p*10+r
#     num=num//10

# if t==p:
#     print("pl")
# else:
#     print("not pl")


# def starpyrmid(n):
    

#     for i in range(n):
#         print(" "*(n-i-1)+"*"*(2*i+1) )


# starpyrmid(3)


# num= int(input("enter a number \n"))
# tem=num
# ar=0
# while num>0:
#     r=num%10
#     ar=ar+r**3
#     num=num//10


# if tem==ar:
#     print("arm")
# else:
#     print("not arm")


# n= int(input("num \n"))
# d1=0
# while n>0:

#     r=n%10
#     if d1<r:
#         d1=r
    
#     n=n//10


# print(d1)



# ch=input("enter a char \n")

# if ch >="A" and ch<="Z":
#     print("uppercase")
# else:
#     print("lowercase")

# y= int(input("num \n"))

# if y%4==0:
#     print(y," is a leap")
# else:
#     print(y," is not a leap year")


# ch=input("enter a char \n")

# if ch in "aeiou":
#     print("vowel")
# else:
#     print("constant")




# p=int(input("enter marks of physics"))
# c=int(input("enter marks of chemistry "))
# m=int(input("enter marks of math"))
# e=int(input("enter marks of english"))
# h=int(input("enter marks of hindi"))
# total=(p+c+m+e+h)
# per=(total*100)/500

# print(total, "\n", per)
# if per>=60:
#     print("grade A")
# elif per>=50:
#     print("grade B")
# elif per>=40:
#     print("grade C")
# elif per<40:
#     print("grade D")


# cu_unit=int(input("enter current month unit \n"))
# lu_unit=int(input("enter last month unit \n"))


# if cu_unit<=150:
#     print(cu_unit*4)
# elif cu_unit<=300:
#     print(cu_unit*6)
# elif cu_unit<=500:
#     print(cu_unit*8)
# else:
#     print(cu_unit*10)

# bs=int(input("enter your basic salary\n"))

# if bs<=15000:
#     ta=(bs*8)/100
#     da=(bs*4)/100
#     print(bs+da+ta)
# else:
#     ta=(bs*10)/100
#     da=(bs*5)/100
#     print(bs+da+ta)



# dic={1:"a" ,2:"e",3:"i",4:"o",5:"u"}
# ch=input("enter char")

# if dic[1]==ch:
#     print(ch,"is vowel")
# elif dic[2]==ch:
#     print(ch,"is vowel")
# elif dic[3]==ch:
#     print(ch,"is vowel")
# elif dic[4]==ch:
#     print(ch,"is vowel")
# elif dic[5]==ch:
#     print(ch,"is vowel")
# else:
#     print("cosntant")


# n=int(input("enter a no "))
# t=n

# for i in range(n-1,0,-1):

#     f=t*i
#     t=f
#     print(i,end=',')


# print("=",f)

# def squareno(n):

#     for i in range(1,n):
#         print(i**2) 

# squareno(11)



# def table(n):

#     for i in range(1,11):

#         print(f"{n} X {i} = {n*i}")


# table(4)

# n=int(input("enter a number \n"))
# rv=0
# temp=n
# ar=0
# for  i in range(n,0,-1):
    
#     if n==0:
#         break

#     r=n%10
#     rv=rv*10+r
#     ar=ar+r**3
#     n=n//10
# if temp==rv:
#     print("palindrom")
# else:
#     print("not a palindrom")


# if temp==ar:
#     print("armstrong ")
# else:
#     print("not a armstrong")
    
# print(rv)
# print(ar)


# n=int(input("enter a number \n"))

# for i in range(1,n):
#     if n%i==0:
#         print(i)


# n=int(input("enter a num \n"))
# sum=0
# temp=n
# for i in range(1,n):

#     if n%i==0:
#         sum=sum+i
        

#         print(i)


# if temp==sum:
#     print("perfect")
# else:
#     print("not perfect")

# n=int(input("enter num \n"))
# fst=0
# sec=1
# sum
#  print(fst,sec,end=" ")
# for i in range(2,n+1):


#     nxt=fst+sec
#     print(nxt,end=" ")
#     fst=sec
#     sec=nxt



# print(nxt)

# 0,1,1,2,3,5,8...


# n=int(input("enter num \n"))
# s=0
# for i in range(n,0,-1):
    
#     if n==0:
#         break

#     r=n%10
#     s=s+r
#     n=n//10
# print(s)

    

# n=int(input("enter num \n"))

# s=0
# for i in range(1,n+1):
#     s=s+(i**2)


# print(s)


# n=int(input("enter num \n"))

# e=0
# o=0
# for i in range(1,n+1):

#     if i%2!=0:
#         e=e+1
#     else:
#         o=o+1


# print(f"form 1 to {n} {e} are even and {o} are odd")

    

# n1=int(input("enter num1 \n"))
# n2=int(input("enter num2 \n"))

# if n1>n2:
#     gr= n1
# else:
#     gr=n2


#     while True:
#         if gr%n1==0 and gr%n2==0:
#             break
#         gr =gr+1

# print(gr)




# n1=int(input("enter num1 \n"))
# n2=int(input("enter num2 \n"))

# if n1>n2:
#     sm=n1
# else:
#     sm=n2

# hfc=0

# for i in range(1,sm+1):
#     if n1%i==0 and n2%i==0:
#         hcf=i



# print(hcf)


# n= int(input("enter a num \n"))
# c=0
# for i in range(2,n+1):
        
#         if n%i==0:
#             c=c+1   

# if c==1:
#     print("prime")
# else:
#     print("not a prime")


# n= int(input("enter a num \n"))
# o=0
# e=0
# for i in range(1,n):

#     if i%2==0:
#         e=e+i
#         print(i,"+",end=" ")
#     else:
#         o=o+i
#         print(i,"-",end=" ")
        


# print("\n =",o-e)


# n= int(input("enter a num \n"))
# s=0

# for i in range(1,n+1):

#     t=i

#     for j in range(i-1,0,-1):

#         t=t*j
#     print(t,end="!")
#     s=s+t



# print("\n =" ,s)


# i=0
# while i<5:
#     print("\n")
    
#     j=0
#     while j<5:
#         print("*",end="")

#         j=j+1
    
#     i=i+1


# i=0
# while i<5:
#     print("\n")
    
#     j=0
#     while j<=i:
#         print("*",end="")

#         j=j+1
    
#     i=i+1
# #



# i=5
# while i>0:
#     print("\n")
    
#     j=5
#     while j>=i:
#         print(j,end="")

#         j=j-1
    
#     i=i-1


# i=1
# while i<=5:
#     print("\n")
    
#     j=1
#     while j<=i:
#         print(j,end="")

#         j=j+1
    
#     i=i+1




i=65
while i<=70:
    print("\n")
    
    j=65
    while j<i:
        print(chr(j),end="")

        j=j+1
    
    i=i+1

    

    






