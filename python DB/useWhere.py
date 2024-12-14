import mysql.connector
mydb =mysql.connector.connect(host="localhost" , username="root", password="root", database="studentdb")
mycursor=mydb.cursor()
query="DELETE from studentinfo WHERE surname='arzare'"
mycursor.execute(query)
mydb.commit()
mycursor.execute(" select * from studentinfo " )
data=mycursor.fetchall()
for i in data:
    print(i)
    mydb.close()