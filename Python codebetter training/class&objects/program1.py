class Areaofrectangle:

    def inputvalue(self,l,b):
        self.lenth=l
        self.breadth=b

        self.lenth=int(input("enter length of rectangle "))
        self.breadth=int(input("enter breadth of rectangle "))
    def calculatevalue(self,a):
        self.areais=a
        self.areais=self.lenth*self.breadth

    def showarea(self):

        print(self.areais)


obj=Areaofrectangle()
obj.inputvalue(4,6)
obj.calculatevalue(1)
obj.showarea()
