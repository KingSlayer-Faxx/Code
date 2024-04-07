import csv

l=[1,2,3,4,5]
m=[[1,2],[3,4],[5,6]]
with open('xyz.csv','w') as file:
    cursor = csv.writer(file)
    cursor.writerow(l)
    cursor.writerows(m)

with open('xyz.csv', 'r', newline='\r\n') as file:
    data = csv.reader(file)
    for i in data:
        print(i)

# search = eval(input('Enter: '))
# with open('xyz.csv','r+') as file:
#     data = csv.reader(file)
#     for i in data:
#         if search == i:
#             print(file.tell())
            # newvalue = int(input("newvalue: "))
