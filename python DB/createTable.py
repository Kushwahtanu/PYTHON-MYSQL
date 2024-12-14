import mysql.connector
mydb =mysql.connector.connect(host="localhost" , username="root", password="root", database="studentdb")
mycursor=mydb.cursor()
mycursor.execute("create table studentinfo (name varchar(20), surname varchar(20), rollno varchar(10))")
print("table created")
