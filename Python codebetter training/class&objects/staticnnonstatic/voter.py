class Voter:

    voterage=18

    def __init__(self,name,age,address):

        self.name=name
        self.age=age
        self.address=address
    def isvoterage(self):
        return bool(self.age>=self.voterage)
    
    def display(self):
        # print()
        print("name: {} |age: {} |address: {}".format(self.name,self.age,self.address))



# obj=Voter('abc',14,'ind')

# obj.display()
# print(obj.isvoterage())



arry=[]
count=0
while True:
    obj=input("enter object name ")
    name=input("name ")
    age=int(input("age "))
    address=input("address ")

    obj=Voter(name,age,address)

    arry.append(obj)

    count=count+1

    if count==2:
        for o in arry:

            o.display()

            print(o.isvoterage())
        break
