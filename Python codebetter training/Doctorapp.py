arayofpatients = [{'name  ': 'abc', 'age': 23, 'gender': 'male', 'weight': 57.0,
                   'vister': 'old', 'Symptoms': 'fever', 'token no': '111'},
                  {'name': 'adf', 'age': 45, 'gender': 'male', 'weight': 56.0,
                   'vister': 'old','Symptoms': 'fever', 'token no': '112'},
                  {'name': 'fork', 'age': 32, 'gender': 'female', 'weight': 65.0,
                   'vister':'old', 'Symptoms': 'cold', 'token no': '113'}
                  ]


for i in arayofpatients:
    print(i)
while True:
    # print(arayofpatients)

    data_dict = {}

    choice = input(
        "enter choice \n options \n 1.)add \n 2.)update \n 3.)remove \n 4.) Sort data \n  ")

    if choice == 'add' or choice == '1':
        add_patient = input("Add new patient ")

        if add_patient.lower() == "y":

            data_dict['name'] = input("enter patient name ")
            data_dict['age'] = int(input("age of patient "))
            data_dict['gender'] = input("enter gender of patient ")
            data_dict['weight'] = float(input("weight of patient "))
            data_dict['vister'] = input(" exiisting patient or new ? ")
            data_dict['Symptoms'] = input("enter symptoms ")
            data_dict['token no'] = input("enter unique token ")
        else:
            break

    elif choice == 'up':
        update = input("do you want to update info ? ")
        if update.lower() == 'y':
            sel = input("token ")

            # data_dict = {}
            for dic in arayofpatients:

                if sel == dic['token no']:
                    dic['name'] = input("update name ")
                    dic['weight'] = int(input("update weight "))
                    break
        else:
            print("no change ")

    elif choice == 'rm':
        remove = input("do you want to remove info type 'y' for yes ")
        if remove.lower() == 'y':
            sel = input("token ")

            # data_dict = {}
            for dic in arayofpatients:

                if sel == dic['token no']:
                    # dic.clear()
                    arayofpatients.remove(dic)
                    break

        else:
            print("no remove yet ")

    elif choice == 'sort':
        sortby = input(
            "sorting by \n token no \n age \n gender \n visit type \n  ")
        if sortby.lower() == 'token':
            def mytk(e):
                return e['token no']

            arayofpatients.sort(key=mytk)
        elif sortby.lower() == 'age':
            def myage(e):
                return e['age']

            arayofpatients.sort(key=myage)

        elif sortby.lower() == 'gender':
            def mygen(e):
                return e['gender']

            arayofpatients.sort(key=mygen)

        elif sortby.lower() == 'vister':
            def myvist(e):
                return e['vister']

            arayofpatients.sort(key=myvist)
    else:
        print("you are out from app")
        break

    # arayofpatients.append(data_dict)
    if data_dict == {}:
        print("data not inserted ")
    else:
        arayofpatients.append(data_dict)

    for i in arayofpatients:
        print(i)
