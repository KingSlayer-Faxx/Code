import pickle

# dump - to save data
# load - to retireve data`
# seek - to move the cursor
# tell - cursor position

l={}

choice = int(input('1. Add Record\n2. Display Records\n3. Search Record\n4. Update Record\nEnter Your Option: '))
if choice == 1:
    with open('xyz.dat','ab') as file:
        l['name'] = str(input("eter stu nme:"))
        l['age'] = str(input("enter age:"))
        l['rollno'] = str(input('enter r no: '))
        pickle.dump(l,file)
        print('Recor Aded')

elif choice==2:
     with open('xyz.dat','rb') as file:
        try:
            while True:
                data = pickle.load(file)
                print(data)
        except EOFError:
            print("yes")

elif choice == 3:
    with open('xyz.dat','rb') as file:
        searchkey = str(input('Enter serch key:'))
        data = pickle.load(file)
        if searchkey in data['rollno']:
            print(data)

elif choice == 4:
    with open('xyz.dat','rb+') as file:
        try:
            searchkey = str(input('Enter serch key:'))
            data = pickle.load(file)
            if searchkey < data['age']:
                x = data['age']
                data['age'] = int(x)+1
                print(data)

        except:
            print('recrd not found')

