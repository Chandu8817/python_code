# a=[12,34]
# print(a,"before swap")
# # a[0],a[1]=a[1],a[0]
# ch=a[0]
# a[0]=a[1]
# a[1]=ch 
# print(a,"after swap")

# qus65
# n=int(input("no of el "))

# a=[ ]
# for  i in range(n):
#     el=int(input("elements "))
#     a.append(el)

# print(a)
# sum=0
# for i in a:
#     sum=sum+i

# print(sum)

# qus66

# a=[12,34,5667,334,56,781,3,4,656,34,7,82]

# max=a[0]

# for i in range(len(a)):


#     if max<a[i]:
#         max=a[i]

# print(max)

# qus67

# a=[12,34,334,56,781,3,4,656,34,7,82]
# l=len(a)

# i=0
# while i<l:

#     j=i+1
#     while j<l:
#         if a[i]<a[j]:
#             ch=a[i]
#             a[i]=a[j]
#             a[j]=ch
#         j=j+1
#     i=i+1
# for k in range(l):
#     print(a[k],end=",")



# qus68

# a=[12,34,56,"hello",45,4]
# b=[2,3,6,"bey",4]
# c=[]
# c.append(a)
# c.append(b)
# print(c)

# for i in a:
    
#     
# for j in b:
#     c.append(j)

# print(c)


# qus69


# a=[12,34,334,56,781,3,4,656,34,7,82]

# # max=a[0]
# for i in range(0,len(a)):
#     for j in range(i+1,len(a)):
#         if a[i]<a[j]:
#             ch=a[i]
#             a[i]=a[j]
#             a[j]=ch

# for i in a:
#     pass

# print("second max is ",a[1])

# qus70


# dic={'stu_name': "rahul",'stu_rollno':"12345",'stu_percent':67.5,
# 'stu_contact':9754467890}
# # print(dic.keys())
# # print(dic.values())

# for x,y in dic.items():
#     print("{} ={} ".format(x,y))

# qus71




# student={ 

#     'ch1':{'std_name':"chandu",
# "std_rollno":123,
# "course":"java",
# "percentage":67},

# 'ch2':{'std_name':"rahul",
# "std_rollno":124,
# "course":"c",
# "percentage":45},

# 'ch3':{'std_name':"ravi",
# "std_rollno":125,
# "course":"rect",
# "percentage":56},

# 'ch4':{'std_name':"don",
# "std_rollno":126,
# "course":"c++",
# "percentage":69},

# 'ch5':{'std_name':"raj",
# "std_rollno":127,
# "course":"python",
# "percentage":61}
# }

# print(student)

# for x,y in student.items():
#     print("{} = {}".format(x,y))




# li=[]



# for i in range(2):
#     dic={}
#     dic['std_name']=input("name ")
#     dic['std_rollno']=int(input("roll no "))
#     dic['course']=input("course ")
#     dic['percent ']=float(input(" percent "))


#     # li=list(dic)
    
#     # dic.update()
#     li.append(dic)

# for i in li:
#     print(i)




# qus=72

# li=[]
# n=int(input("no of data "))
# for i in range(n):
#     dic={}

#     dic["pid"]=int(input("id "))
#     dic["product name"]=input("name ")
#     dic["quantity"]=int(input("quantity "))
#     dic["price"]=float(input("price "))

#     li.append(dic)

# for i in li:
#     print(i)



# qus=73

# li=[]

# n=int(input("dta "))

# for i in range(n):
#     dic={}

#     dic['empid']=int(input("id "))
#     dic['emp_name']=input("name of employe ")
#     dic['salary']=float(input("salary "))

#     li.append(dic)

# for i in li:
#     print(i)


# s="helloworld"
# ch=[]
# for i in s:
#     ch.append(ord(i))
# for i in ch:
#     a=i-32
#     print(chr(a),end=' ')

    
# for i in range(65,91):
#     print(chr(i),end=',')


# qus=75


s=input("enter a string ")
ch=''
for i in s:

    ch=i+ch

if ch==s:
    print("palindrome ")
else:
    print("not a palindrome ")


