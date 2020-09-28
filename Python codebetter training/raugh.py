import pickle

# def data_pick():

#     data= { 'name' : "chandrashekhar",
#             'age': 25,
#             'mob_no' : '9754468769',
#             'college': "svce"
#              }

#     output= open('pick.txt', 'wb')
#     pickle.dump(data,output)
#     output.close()

# # data_pick()
# def data_unpick():

#     file=open('pick.txt', 'rb')
#     new_data=pickle.load(file,)
#     file.close()
#     return new_data

# print(data_unpick())


# def genrator():
#     yield 1
#     yield 2
#     yield 3


# for i in genrator():
#     print(i)
# x=genrator()
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())


# def fibogenrators(limit):

#     a,b=0,1
#     while a<limit:
#         yield a
#         a,b=b,a+b

# x=fibogenrators(6)
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())

# for x in fibogenrators(6):
#     print(x)

import re

print(re.subn('h', '%','hello this is python re module'))
print(re.sub('s','#', 'thiS is the best visusal studio', flags=re.IGNORECASE))
print(re.split('\W', 'hello this is good'))
print(re.split('\d' , ' herlfe 12gh 45fgdh,67rt67'))