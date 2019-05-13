from client_database_connection import mycursor
from config import node_id
import time
time.sleep(5)
def run():
    while True:
        time.sleep(5)
        sql = "SELECT node_free FROM node_data where node_id = " + code_id 
        mycursor.execute(sql)
        check = mycursor.fetchone()
        if(check==1):
            os.system('python node_free.py')

run()
