# # s=input("enter a string ")
s ="3+4*(3*5)+(7+({22)*98-3/(45+3)})"

l = []
l2 = ['(', ')', '{', '}', '[', ']']

dic={
      1:'()',2:'{ }',3:'[]'
    }
l3 = []
for i in s:

    if i not in l2:
        l.append(i)
    else:
        l3.append(i)
c1 = 0
c2 = 0
# l3.sort()
l4=[]
# print(l3)
for i in l3:
    if i == ('(') or i == ('{') or i == ('['):
        c1 += 1
        # l4.append(i)
    elif i == ')' or i == '}' or i == ']':
        c2 += 1



    
print(l4)


if l3[0] == ')' or l3[0] == '}' or l3[0] == '}':
    print("not balanced")
# elif l5==l4:
#     print('not balanced')
elif l3==['(','}']:
    print("not balanced")
elif c1 == c2:
    print("balanced")
else:
    print("not balanced")








































# def parnt(strr):
#     stck=[]

#     for i in range(len(s)):
#         if (s[i]=='(' or s[i]=='{' or s[i]=='[' ):
#             stck.append(s[i])
#             continue
#         if s[i]==')':
#             x=stck.pop()
#             if (x=='}' or  x==']'):
#                 return False
#         elif s[i]=='}':
#             x=stck.pop()
#             if (x==')' or  x==']'):
#                 return False
#         elif s[i]==']':
#             x=stck.pop()
#             if (x==')' or  x=='}'):
#                 return False
#     print(stck)
# if (parnt(s)):
#     print('balanced')
# else:
#     print('not balanced')

