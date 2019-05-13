
import getpass
# imports
import os

from client_database_connection import mycursor
from config import free

# functions
def effect():
    os.system("cls")
    print('''
    __          ________      _    _  ____   _____ _______
    \ \        / /  ____|    | |  | |/ __ \ / ____|__   __|
     \ \  /\  / /| |__ ______| |__| | |  | | (___    | |
      \ \/  \/ / |  __|______|  __  | |  | |\___ \   | |
       \  /\  /  | |____     | |  | | |__| |____) |  | |
        \/  \/   |______|    |_|  |_|\____/|_____/   |_|

     ''')


def input():
    # get data
    database_ip = input("Database IP:-")
    database_name = input("Database Name:-")
    database_user = input("Database User:-")

    try:
        database_password = getpass.getpass()
    except Exception as error:
        print('ERROR', error)
        print("please contact developer")

    node_id = input("Node ID:- ")
    try:
        node_password = getpass.getpass()
    except Exception as error:
        print('ERROR', error)
        print("please contact developer")

    print("Connecting to database")
    print('Database ip :-' + database_ip)
    print('Database name :-' + database_name)
    print('Database User :-' + database_user)
    print("Database Password:-************")
    print("Node id:- " + node_id)
    print("Password:-************")
    mydb = mysql.connector.connect(
        host=database_ip,
        user="root",
        passwd=database_password,
        database=database_name
    )
    print(mydb)
    mycursor = mydb.cursor()
    sql = "SELECT node_password FROM node_data where node_id =" + node_id
    mycursor.execute(sql)
    Password = mycursor.fetchone()
       if(node_password == Password):
            auth = True
            local_path=os.getcwd()
            ftp_ip = input("Ftp ip")
            ftp_user = input("Ftp username")
            ftp_password = input("Ftp password")
            config = {}
            config['data'] = []
            data['people'].append({
                'database ip': database_ip,
                'database name': database_name,
                'database user': database_user,
                'database password': database_password,
                'node id': node_id,
                'node password': node_password,
                'ftp ip': ftp_ip,
                'ftp username': ftp_user,
                'ftp password': ftp_password
                'local path' : local_path
            })

            with open('config.json', 'w') as outfile:
                json.dump(config, outfile)
            free = True
            return auth
        else:
            print("Error Authendication failed")
            auth = False
            return auth


# code
effect()
input()
if(auth == True):
    print("starting local-host....")

    command = 'python requirements.py'
    os.system(command)
else:
    effect()
    input()
