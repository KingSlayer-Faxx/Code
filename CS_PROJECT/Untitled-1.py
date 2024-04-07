with open('gh.txt','r') as file:
    data = file.readlines()
    for i in data:
        if i.startswith('the'):
            with open('ab.txt','a') as file2:
                file2.write(i)


with open('gh.txt','r') as file:
    data = file.readlines()
    print(len(data))
    upper=0
    lower=0
    for i in data:
        for j in i:
            # print(upper,lower)
            if j.isupper():
                upper+=1
            else:
                lower+=1
print(upper)
print(lower)


import mysql.connector as mc

mydb = mc.connect(host = 'localhost', user = 'libmansys', passwd = 'libmansys', database = 'lib')
print(mydb.is_connected())

mycursor = mydb.cursor()


mycursor.execute('select * from library')
data = mycursor.fetchall()
print(data)