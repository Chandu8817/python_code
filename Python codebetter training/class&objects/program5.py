class Studentinfo:

    def __init__(self,stdnm,stdid,stdper):
        self.id=stdid
        self.name=stdnm
        self.percent=stdper

    
    def showstdinfo(self):
        print("the name of student is {} \n and his roll no is {} \n or percent is {}".format(self.name,self.id,self.percent))
    

obj1=Studentinfo('abc',123,56)
obj1.showstdinfo()
obj2=Studentinfo('xyz',122,67)
obj2.showstdinfo()