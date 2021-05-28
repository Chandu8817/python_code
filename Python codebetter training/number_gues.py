import random

while (True):
    print("do you want to quit the game")

    sys_num = random.randrange(1, 30)
    print(sys_num)

    try:
        num = input("enter a number \n ")
        if num == "q":
            break
        else:

            n = int(num)

            if n == sys_num:
                print("you won you gusse right number")

            else:

                print("wrong num try again .,,,")

    except Exception as e:
        print("you enter invaild digit ")
