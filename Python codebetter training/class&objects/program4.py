class Addition:

    def add(self):
        a=12.5
        b=15.34
        c=45.7
        print(a,b,c)

class Another(Addition):
    
    def add(self):
        a=[1,2,3,4,5]
        print(a)
class third(Addition):
    def add(self):
        a=12
        b=34
        print(a,b)

obj=Addition()
obj.add()
obj1=Another()
obj1.add()
obj2=third()
obj2.add()
