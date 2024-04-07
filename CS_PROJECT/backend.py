import  csv
with open("BookInfo.csv",'r') as file:
    csvreader=csv.reader(file)
    for row in csvreader:
        print(row)

import mysql.connector
mydb = mysql.connector.connect(host='127.0.0.1',user='root',passwd='',db='trial')
cursor = mydb.cursor()
file=open("Hillwoods Acc. Register.xls - Sheet1.csv",'r')
csvreader = csv.reader(file)
for row in csvreader:
    if row[0] == 'Acc. No.':
        pass
    else:
        for i in row:
            if i == "":
                row[row.index(i)] = 0
            if i == "#":
                row[row.index(i)] = 0
        sql = f"INSERT INTO bookinfo (Acc_No, Class_No, Title, Author, Publisher, Year, Pages, Author_initial, Volume, Net_Amount, Copies, CD) VALUES {tuple(row)}"
        print(sql)
        try:
            cursor.execute(sql)
        except:
            mydb.commit()
mydb.commit()    
mydb.close()
