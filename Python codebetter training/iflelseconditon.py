# n1=int(input("no 1st "))
# n2=int(input("no 2nd "))

# if n1%n2==0:
#     print("no is divisbalbe")
# else:
#     print("no is not divsiable")


# qus17

# n=int(input("no "))
# if n%2==0:
#     print("even")
# else:
#     print("odd")

# qus=18

# n1=int(input("no 1st "))
# n2=int(input("no 2nd "))

# if n1>n2:
#     print( n1," is biggest")
# else:
#     print(n2," is biggest")

# qus=19

# n1=int(input("no 1st "))
# n2=int(input("no 2nd "))
# n3=int(input("no 3rd "))

# if n1>(n2 and n3):
#     print( n1," is biggest")
# elif n2>(n1 and n3):
#     print(n2," is biggest")
# else:
#     print(n3," is biggest")


# qus20

# n=int(input("enter a no "))
# temp=n
# ans=0
# r=n%10
# ans=ans*10+r

# n=n//10
# r=n%10
# ans=ans*10+r

# n=n//10
# r=n%10
# ans=ans*10+r

# if ans==temp:
#     print("palindrom")
# else:
#     print("not a palindrom")



# qus-21

# n=int(input("enter a no "))
# temp=n
# arm=0
# r=n%10
# arm=arm+(r**3)
# n=n//10

# r=n%10
# arm=arm+(r**3)
# n=n//10
# r=n%10
# arm=arm+(r**3)
# if arm==temp:
#     print("armstrong")
# else:
#     print("not a armstrong")

# qus-22

# n=int(input("no "))

# r1=n%10
# n=n//10
# r2=n%10
# n=n//10
# r3=n%10


# if r1>(r2 and r3):
#     print( r1," is biggest")
# elif r2>(r1 and r3):
#     print(r2," is biggest")
# else:
#     print(r3," is biggest")



# qus-23

# age=int(input("age of person "))
# if age>=18 and age<=100:
#     print("can vote ")
# else:
#     print(" not eligible for vote")



# qus-24

# n=int(input("number  "))
# if n>0:
#     print("positive")
# elif n==0:
#     print(" zero")
# else:
#     print("negative")

# qus=25



# chr=input("enter alphabet ")
# if chr>='a' and chr<='z':
#     print(chr,'is lowercase')
# elif chr>='A'and chr<='Z':
#     print(chr,"uppercase")
# else:
#     print('spical or num')


# qus=26

# y=int(input("year "))

# if y%4==0:
#     print("leap year")
# else:
#     print("not a leap year")



# qus=27

# chr=input("enter char ")

# if chr=='a'or chr=='e' or chr=='i'or chr=='o' or chr=='u':
#     print("vowel")
# else:
#     print("constant")


# qus=28

# p=int(input("marks "))
# m=int(input("marks "))
# c=int(input("marks "))
# e=int(input("marks "))
# h=int(input("marks "))

# total=p+m+c+e+h
# per=total/5
# print("the total marks is ",total)
# print(" the percentage is ",per)

# if per>=60:
#     print("A Grade")
# elif per>=50:
#     print("B Grade")
# elif per>=40:
#     print("C Grade")
# elif per<40:
#     print("D Grade")
# else:
#     print("wrong op")


# qus-29


# unitlst= int(input("enter last month unit"))
# unitcrt= int(input("enter current month unit"))

# if unitcrt<=150:
    
#     print("you bill is rupee ",unitcrt*4)
# elif unitcrt>150 and unitcrt<=300:
#     print("you bill is rupee ",unitcrt*6)
# elif unitcrt>300 and unitcrt<=500:
#     print("you bill is rupee ",unitcrt*8)
# else:
#     print("you bill is rupee ",unitcrt*10)
    

# qus=30

# bs=int(input("enter basic salary "))

# if bs<=15000:
#     ta=bs*8/100
#     da=bs*4/100
#     print("the gross slary is ", bs+ta+da)
# elif bs>15000:
#     ta=bs*10/100
#     da=bs*5/100
#     print("the gross slary is ", bs+ta+da)
# else:
#     print("Wrong input")

# qus=31


# chr=input("enter chr ")

# dic={1:'a',2:'e',3:'i',4:'o',5:'u'}

# if chr==dic[1]:
#     print("vowel")
# elif chr==dic[2]:
#     print("vowel")
# elif chr==dic[3]:
#     print("vowel")
# elif chr==dic[4]:
#     print("vowel")
# elif chr==dic[5]:
#     print("vowel")
# else:
#     print("not a vowel")

# qus 32

# week_no=int(input("enter no in week "))

# dic={1:'monday',2:'tusday',3:'wednesday',4:'thusday',5:'friday',6:'satarday',7:'sunday'}

# if week_no==1:
#     print(dic[1])
# elif week_no==2:
#     print(dic[2])
# elif week_no==3:
#     print(dic[3])
# elif week_no==4:
#     print(dic[4])
# elif week_no==5:
#     print(dic[5])
# elif week_no==6:
#     print(dic[6])
# elif week_no==7:
#     print(dic[7])
# else:
#     print("wrong input")

# qus=33


# month_no=int(input("enter no in month "))

# dic={1:'january',2:'feburary',3:'march',4:'april',5:'may',6:'june',7:'july',8:'augast',9:'september',10:'october',11:'novmeber',12:'december'}

# if month_no==1:
#     print(dic[1])
# elif month_no==2:
#     print(dic[2])
# elif month_no==3:
#     print(dic[3])
# elif month_no==4:
#     print(dic[4])
# elif month_no==5:
#     print(dic[5])
# elif month_no==6:
#     print(dic[6])
# elif month_no==7:
#     print(dic[7])
# elif month_no==8:
#     print(dic[8])
# elif month_no==9:
#     print(dic[9])
# elif month_no==10:
#     print(dic[10])
# elif month_no==11:
#     print(dic[11])
# elif month_no==12:
#     print(dic[12])
# else:
#     print("wrong input")


op=input("enter option ")
a=int(input("no1 "))
b=int(input("no2 "))
dic={'+':(a+b),'-':(a-b),'*':(a*b), '/':(a/b)}

if op=='+':
    print(dic['+'])
elif op=='-':
    print(dic['-'])
elif op=='*':
    print(dic['*'])
else:
    print(dic['/'])