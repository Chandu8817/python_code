class Cricket:
    def __init__(self,p_name,t_name,b_avg):
        self.pn=p_name
        self.tn=t_name
        self.ba=b_avg

    def display(self):
        print("{} | {} | {}".format(self.pn,self.tn,self.ba))


obj1=Cricket("virat","India",59.35)
obj1.display()


while True:
    o=input("enter obj ")
    n="virat"
    
