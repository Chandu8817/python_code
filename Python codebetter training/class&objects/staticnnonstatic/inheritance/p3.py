class BankAccount:

    def __init__(self, account_no, balance):

        self.account_no = account_no
        self.balance = balance

    def Display(self):
        print(self.account_no, self.balance)

    def DepositAmount(self, a: float):
        self.a = a
        self.balance = self.balance+self.a

    def WithdrawAmount(self, a: float):
        self.a = a
        self.balance = self.balance-self.a


class SavingAccount(BankAccount):

    minmumbalance = 2000

    def __init__(self, cust_name, cust_address, account_no, balance):
        self.cust_name = cust_name
        self.cust_address = cust_address

        super().__init__(account_no, balance)

    def WithdrawAmount(self, a: float):
        self.a = a

        if self.balance <= self.minmumbalance:
            print("your account balance is low")
        else:
            self.balance = self.balance-self.a

    def Display(self):

        print(self.cust_name, self.cust_address, self.account_no, self.balance)


class CurrentAccount(BankAccount):

    overdarftlimit = 5000

    def __init__(self, shop_name, shop_address, account_no, balance):

        self.shop_name = shop_name
        self.shop_address = shop_address

        super().__init__(account_no, balance)

    def Display(self):
        print(self.shop_name, self.shop_address, self.account_no, self.balance)

    def WithdrawAmount(self, a: float):
        self.a = a
        if (self.a <=self.overdarftlimit or self.a < self.balance) and (self.balance >= -5000):
            self.balance = self.balance-self.a

        else:
            print("your limmit is over ")


obj1 = CurrentAccount('Shop2', 'dewas', 12345, 3000)
obj2 = SavingAccount('chandu', 'indore', 3245, 1000)
obj3 = CurrentAccount('shop1', 'indore', 881780, 0)



banklist = [obj1,obj2,obj3]
    
for i in banklist:
    i.Display()
while True:


    option = input("enter inputs ")

    if option == 'add':

        obj = input("name of object ")
        name = input("enter name ")
        address = input("enter address ")
        accno = int(input("enter acc no "))
        balance = float(input("enter balance"))

        op = input("which type of account ")

        if op == 'saving':

            obj = SavingAccount(name, address, accno, balance)
            banklist.append(obj)
            for i in banklist:
                i.Display()

        elif op == 'current':
            obj = CurrentAccount(name, address, accno, balance)
            banklist.append(obj)
            for i in banklist:
                i.Display()
        else:
            print("account type not found")


    elif option == 'dp':
        accno = int(input("enter account no "))

        for l in banklist:
            if l.account_no == accno:
                amt = float(input("enter withdraw amount "))
                l.DepositAmount(amt)
        for l in banklist:
            l.Display()
    
    elif option == 'wd':
        accno = int(input("enter account no "))
        for l in banklist:   
            if l.account_no == accno:
                amt = float(input("enter withdraw amount "))
                l.WithdrawAmount(amt)
        for l in banklist:
            l.Display()


    else:
        print("error")
        break
