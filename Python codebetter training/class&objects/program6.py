class Employe:

    name="rohan"
    def __init__(self,id,salary):
        self.id=id
        self.salary=salary
    def show(self):

        print(self.name,self.id,self.salary)


obj=Employe(123,40000)
obj.show()


        