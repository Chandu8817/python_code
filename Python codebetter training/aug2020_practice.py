

# n= int(input("enter num"))
# t=n
# sum=0
# while n>0:

#     r= n%10

#     sum=sum+r


#     n=n//10

# print(f"the sum of {t} digits is {sum}")


# num = int(input("enter a num "))

# for i in range(num):

#     if 2**i== num:
#         print(f"the {num} is power of 2")
#         break
# else:
#     print(f"the {num} is not a power of 2")


# num = int(input("enter a num"))


# for i in range(1,num):

#     if num%i==0:
#         print(i)


# name = input("enter a string ")

# t=""


# for i in name:

#     t = i+t

# if name==t:
#     print("string is palindrom")
# else:
#     print("given string not a palindram")


# str_1= input("enter a string-1  \n")
# str_2= input("enter a string-2  \n")


# list_a=[]
# list_b=[]

# for i in str_1:
#     list_a.append(i)
# for i in str_2:
#     list_b.append(i)

# if sorted(str_1)==sorted(str_2):

#     print("anagram")
# else:
#     print("not a anagram")


# list_a = [2, 6, 3, 7, 2, 8, 1, 5]

# sum = 9
# list_b = []

# for i in range(len(list_a)):

#     for j in range(i+1, len(list_a)):

#         if list_a[i]+list_a[j] == sum:

#             list_b.append(list_a[i])
#             list_b.append(list_a[j])


# print(list_b)


# try:
#     n= int(input("enter a num"))

#     ns=str(n)
#     lst=[]

#     for i in ns:
#         lst.append(int(i))


# except Exception as e:
#     print("negatvie not alowed")

# else:

#     for i in lst:
#         if i>1:
#             print(f"{n} is not binary")
#             break
#     else:
#         print(f"{n} is binary")


# n= 100

# for i in range(1,n):

#     j=i
#     c=0

#     for k in range(j,0,-1):

#         if i%k==0:
#             c=c+1
    
#     if c==2:
#         print(i)

    

s= input("enter string ")

s1=[]
s2=[]

for i in s:

    if i not in s1:
        s1.append(i)
    elif i not in s2:
        s2.append(i)
    

print(f" duplicate char in {s} are {s2}")



    