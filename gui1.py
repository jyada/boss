import mysql.connector 
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="remo"
)

print(mydb)