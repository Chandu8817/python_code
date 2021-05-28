class Books:
    discountrate=15
    count=0
    
    def __init__(self,tittle,price):
        self.tittle=tittle
        self.price=price

    def calculatediscount(self,finalprice):
        self.finalprice=finalprice
        self.finalprice= self.price-(self.price*self.discountrate/100)
        

    def Display(self):
        self.count=1+self.count

        
        print("count: {} | Book name: {} | price: {} | discount: {} | final price: {}".format(self.count,self.tittle,self.price,self.discountrate,self.finalprice))
        
       



    
l=[]
# obj=Books('mathmatics',230)
# obj.calculatediscount(1)
# obj.Display()
# l.append(obj)




while True:
    # for i in l:
    #     i.Display()

    op=input("enter option to add new book, calculate total of all books ")

    if op=="add":
        objec=input("name of buyer")
        title=input("enter book name ")
        price=float(input("enter book price "))
        objec=Books(title,price)
        objec.calculatediscount(1)
        l.append(objec)

        for i in l:
            i.Display()
    
    elif op=='total':
        sum=0

        for b in l:
            sum=sum+b.finalprice
        print(sum)
