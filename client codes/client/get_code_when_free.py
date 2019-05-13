from client_database_connection import mycursor
from ftp import *
from config import free , node_id, local_path


while free:
    sql = "SELECT code_id FROM code_node where node_id = " + node_id
    mycursor.execute(sql)
    node = mycursor.fetchone()
    code_id = mycursor.fetchone()
    if(code_id is not None):
        break


hostname = ftp_hostname()
password = ftp_password()
user = ftp_user()

sql = "SELECT code_path FROM code_data where code_id = " + code_id 
    mycursor.execute(sql)
    remote_path = mycursor.fetchone()

connect(hostname, user , password ,local_path ,remote_path)



