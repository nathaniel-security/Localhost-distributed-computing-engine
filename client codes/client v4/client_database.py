import mysql.connector
import json

with open('config.json') as json_file:  
    data = json.load(json_file)
    for p in data['config']:
        database_ip = p['database ip']
        database_user=p['database user']
        database_password=p['database password']
        database_name=p['database name']



mydb = mysql.connector.connect(
          host=database_ip,
          user=database_user,
          passwd=database_password,
          database=database_name
        )

mycursor = mydb.cursor()
