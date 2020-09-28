class Employe:

    def __init__(self,id,name,salary):

        self.id=id
        self.name=name
        self.salary=salary
    
    def Display(self):
        print("Id : {} | name : {} | salary : {}".format(self.id,self.name,self.salary))

    
class ParttimeEmploye(Employe):

    def __init__(self,id,name,salary,hourworked,hourlyrate):

        self.hourworked=hourworked
        self.hourlyrate=hourlyrate

        super().__init__(id,name,salary)

        print("parttime employe ",self.hourworked, "works ","at rate of  ",self.hourlyrate)
    
    def Calculatesalary(self):

        self.salary=(self.hourlyrate*self.hourworked)*30
    


class FulltimeEmploye(Employe):

    def __init__(self,id,name,salary,basic,da,pf):

        self.basic=basic
        self.da=da
        self.pf=pf
        super().__init__(id,name,salary)


    def Calculatesalary(self):

        self.da=self.basic*15/100
        self.pf=(self.basic+self.da)*12/100
        self.salary=self.basic+self.da-self.pf

def gettax(obj):
    tax=obj.salary*12.5/100
    return ("income tax on salary is ", tax)




obj3=Employe(12223,'abc',20000)
obj3.Display()
print(gettax(obj3))
print('\n')

obj1=ParttimeEmploye(1234,'xyx',12,4,200)
obj1.Calculatesalary()
obj1.Display()
print(gettax(obj1))
print("\n")
obj2=FulltimeEmploye(123,'abc','',35000,'','')
obj2.Calculatesalary()
obj2.Display()
print(gettax(obj2))
