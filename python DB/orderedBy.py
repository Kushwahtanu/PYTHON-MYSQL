import mysql.connector
mydb =mysql.connector.connect(host="localhost" , username="root", password="root", database="studentdb")
mycursor=mydb.cursor()
query="select * from studentinfo ORDER BY rollno"
mycursor.execute(query)
mydata=mycursor.fetchall()
for i in mydata:
    print(i)