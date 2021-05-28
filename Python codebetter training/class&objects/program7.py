class Farmer:

    def __init__(self,name,crop,earning):

        self.name=name
        self.crop=crop
        self.earning=earning

    def display(self):
        print('name : {} \n crop : {} \n earning : {}'.format(self.name,self.crop,self.earning))




obj1=Farmer('ram','wheat',80000.00)
obj2=Farmer('shyam','corn',120000.00)

if obj1.earning > obj2.earning:
    obj1.display()
else:
    obj2.display()
