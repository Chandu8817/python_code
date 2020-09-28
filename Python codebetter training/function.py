# qus=58

# def prime(n):

#     c=0
#     for i in range(1,n+1):

#         if n%i==0:
#             c=c+1
    
#     if c==2:
#         print(n,"is prime")
#     else:
#         print(n,"not prime")
# num=int(input("no "))
# prime(num)


# qus=59 (61 is same) 

# def fact(n):

#     if n==1:
#         return n
#     elif n<=0:
#         return n
#     else:
#         return n*fact(n-1)

# num=int(input("no "))
# print(fact(num))

# qus=60

# def swap(n1,n2):

#     print(n1,n2 ,"before swap")
#     n1,n2=n2,n1
#     return "n1= ",n1, "and  n2= ",n2, " after swap"

# print(swap(23,45))

# def summ(n):
#     sum=0
    
#     if n<=0:
#         return 0
#     else:
        
#         r=n%10
#     sum=sum+r
#     return (sum+(summ(n//10)))
    
# num=int(input("no "))
# print(summ(num))
        
def fibo(n):
    a=0
    b=1
    c=a+b
    print(a,b,c)

    for i in range (0,n-2):
        
        a=b
        b=c
        c=a+b
    
        print(c,end=',')      
    
            

    

(fibo(6))