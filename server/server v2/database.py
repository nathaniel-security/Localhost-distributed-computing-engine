import mysql.connector

database_ip = 'localhost'
database_user = "root"
database_password = ""
database_name = "we_host_data"



mydb = mysql.connector.connect(
          host=database_ip,
          user=database_user,
          passwd=database_password,
          database=database_name
        )

mycursor = mydb.cursor()
