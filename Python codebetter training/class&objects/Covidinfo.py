class Covid19:
    def __init__(self,state,city,name,age,patientid):
        self.state=state
        self.city=city
        self.name=name
        self.age=age
        self.patientid=patientid
    def show(self):
        print( " {}   {} {}  {}   {}".format(self.state,self.city,self.name,self.age,self.patientid))


obj1=Covid19('MP','Indore','Boot1',56,1)
obj1.show()

data=[]
while True:
    for i in data:
        i.show()
    op=input("enter option ")
    if op=='add':
        obj=input('enter obj name')
        s=input('state name')
        c=input('city name')
        n=input('paitent name ')
        a=int(input("enter age "))
        id=int(input('paitent id '))
        data_dict['State'] = s
        data_dict['City'] = c
        data_dict['Name'] = n
        data_dict['age'] = a
        data_dict['id'] = id
        obj=Covid19(s,c,n,a,id)
        data.append(obj)

