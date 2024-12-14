import mysql.connector
mydb =mysql.connector.connect(host="localhost" , username="root", password="root")
mycursor=mydb.cursor()
mycursor.execute("create database if not exists studentdb")
print("database created")
