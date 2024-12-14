import mysql.connector
mydb=mysql.connector.connect(host='localhost', username='root', password='root', database='studentdb')
mycursor=mydb.cursor()
query="UPDATE studentinfo SET name='pari'  WHERE name='tanisha' "
mycursor.execute(query)
mydb.commit()
mycursor.execute("select * from studentinfo")
data=mycursor.fetchall()
for i in data:
    print(i)
mydb.close()

    
