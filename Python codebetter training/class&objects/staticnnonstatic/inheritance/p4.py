import abc

class Flyingstyle(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def fly(self):

        pass


class Bird(Flyingstyle):

    def __init__(self,name,habitat,food,fcolor):

        self.name=name
        self.habitat=habitat
        self.food=food
        self.fcolor=fcolor

    def Dispaly(self):
        print(self.name,self.habitat,self.food,self.fcolor)

    def fly(self):

        return (self.name, "can fly high")


obj=Bird('parriot','chii','chilly','green')
obj.Dispaly()
x=obj.fly()
print(x)