import mysql.connector
mydb =mysql.connector.connect(host="localhost" , username="root", password="root", database="studentdb")
mycursor=mydb.cursor()
query="insert into studentinfo(name , surname, rollno ) values( %s,%s,%s) "
name=input("Enter your name")
surname=input("Enter your surname")
rollNumber=input("Enter your rollnumber")
mycursor.execute(query, (name, surname, rollNumber))
mydb.commit()
print("data inserted")

