n=int(input("enter num "))

for i in range(1,n):

    if 2**i==n:
        print('given no is power of 2')
        break

else:
    print("num is not")