class Student:

    def inputinfostd(self,sn,sid,spercent):

        self.s=sn
        self.id=sid
        self.sp=spercent

        self.s=input("enter name of student ")
        self.id=int(input("enter student id no "))
        self.sp=float(input("enter percentage of student "))

    def outputstddata(self):
        print(self.s)
        print(self.id)
        print(self.sp)

obj=Student()

obj.inputinfostd('sn',1,1.2)
obj.outputstddata()
