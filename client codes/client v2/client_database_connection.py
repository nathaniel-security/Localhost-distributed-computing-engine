import mysql.connector

config = json.loads(open('config.json').read())
ip = config['database ip']
database_name = config['database name']
database_user = config['database user']
database_password = config['database password']
mydb = mysql.connector.connect(
    host=ip,
    user=database_user,
    passwd=database_password,
    database=database_name
)

print(mydb)

mycursor = mydb.cursor()
