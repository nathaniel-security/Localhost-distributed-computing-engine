import mysql.connector

mydb = mysql.connector.connect(
    host=database_ip,
    user=database_user,
    passwd=database_password,
    database=database_name
)

print(mydb)

mycursor = mydb.cursor()
