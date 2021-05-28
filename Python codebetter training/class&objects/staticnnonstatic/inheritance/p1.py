class Student:

    def __init__(self,name,course,dob):
        self.name=name
        self.course=course
        self.dob=dob
        print(self.name,self.course,self.dob)


print('\n \n')
class SchoolStudent(Student):

    def __init__(self,name,course,dob,fees):
        
        super().__init__(name,course,dob)
        self.fees=fees
        print(self.fees)

class CollegeStudent(Student):

    def __init__(self,name,course,dob,sem,fees):
        self.sem=sem
        self.fees=fees
        super().__init__(name,course,dob)
        
        print(self.sem,self.fees)
class PGstudent(CollegeStudent):

    def __init__(self,name,course,dob,sem,fees,mainsubject,percent):

        super().__init__(name,course,dob,sem,fees)

        self.mainsubject=mainsubject
        self.percent=percent

        print(self.mainsubject,self.percent)



obj1=Student('chandu','','10/jan/1995')

obj1=SchoolStudent('chandu','MAths','10/jan/1995',7000)
obj1=CollegeStudent('chandu','BE','10/jan/1995','8th sem',40000)
obj1=PGstudent('chandu','','10th jan 1995','',60000,'python',80.5)

