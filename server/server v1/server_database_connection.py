import mysql.connector
print("step one done")
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="we_host_data"
)

print(mydb)

mycursor = mydb.cursor()