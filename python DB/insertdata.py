import mysql.connector
mydb =mysql.connector.connect(host="localhost" , username="root", password="root", database="studentdb")
mycursor=mydb.cursor()
mycursor.execute("insert into studentinfo(name , surname, rollno ) values('tanisha' ,' kushwah',' 1012 ') ")
mydb.commit()
print("data inserted")
