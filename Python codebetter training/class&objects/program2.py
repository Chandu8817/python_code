class Demoarthmetic:

    def inputs(self,x,y):
        self.no1=x
        self.no2=y

        self.no1=int(input("enter first No "))
        self.no2=int(input("enter second No "))
    def addition(self,a):
        self.add=a
        self.add=self.no1+self.no2
    def subtraction(self,s):
        self.sub=s
        self.sub=self.no1-self.no2
    def multiply(self,m):
        self.mul=m
        self.mul=self.no1*self.no2
    def divide(self,d):
        self.div=d
        self.div=self.no1/self.no2

    def result(self):
        print(self.add)
        print(self.sub)
        print(self.mul)
        print(self.div)
obj=Demoarthmetic()

obj.inputs(1,2)
obj.addition(1)
obj.subtraction(2)
obj.multiply(3)
obj.divide(4)
obj.result()