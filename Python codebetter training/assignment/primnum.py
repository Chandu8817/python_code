n=int(input("enter num range "))



for i in range(1,n+1):

    j=i
    c=0
    for k in range(j,0,-1):
        if i%k==0:
            c=c+1


    if c==2:
        print(i)
# i=1
# while i<=n:
#     j=i
#     c=0
#     while j>=1:
#         if i%j==0:
#             c=c+1

#         j=j-1


    # if c==2:
    #     print(i)

    # i=i+1
