n=int(input("enter a number "))

t=n

for i in range(n,1,-1):
    print(i,end='*')
    
    t=t*(i-1)
    

print("1 =",t)
