class BankAcount:

    def __init__(self,accountno,name,balance):
        self.accountno=accountno
        self.name=name
        self.balance=balance


    def Deposit(self,add):
        self.add=add
        self.add=float(input("enter deposit amount "))

        self.balance=self.balance+self.add
    
    def Withdraw(self,sub):
        self.sub=sub
        self.sub=float(input("enter withdraw amount "))
        self.balance=self.balance-self.sub
    def Display(self):
        a=[self.accountno,self.name,self.balance]

        print(a)




obj1=BankAcount(103,'abc',4000)
obj2=BankAcount(102,'pql',5000)
obj3=BankAcount(105,'xyz',7000)
obj4=BankAcount(106,'mnp',3000)
obj5=BankAcount(101,'stu',9000)




l=[]
l.append(obj1)
l.append(obj2)
l.append(obj3)
l.append(obj4)
l.append(obj5)

# print(l)


while True:
    print('AccountNo |Name |Balance')
    for o in l:
        o.Display()

    
    op=input("enter option ")
    

    if op=="add":
        objec=input("object name ")
        id=int(input("id "))
        name=input("name ")
        amt=float(input('amount '))
        objec=BankAcount(id  ,  name,  amt)
        l.append(objec)

    elif op=='ds':
        # se=input("display by ")

        
            # if se=='a no':
        l.sort(key=lambda x: x.accountno)
                
            
        
    elif op=='dp':
        acc_no=int(input("enter account no "))
        for d in l:
            
            if acc_no==d.accountno:
                d.Deposit(1)
                d.Display()

    elif op=='wd':
        acc_no=int(input("enter account no "))
        for d in l:
            
            if acc_no==d.accountno:
                d.Withdraw(1)
    
    elif op=='del':
        acc_no=int(input("enter account no "))
        for d in l:
            if acc_no==d.accountno:
                l.remove(d)
    else:
        print("thankyou see you next time")
        break
        
            
        


# obj.Withdraw(2)
# obj.Display()
# obj.Deposit(1)
# obj.Display()
