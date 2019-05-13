import getpass
import mysql.connector
import os

print('''
__          ________      _    _  ____   _____ _______ 
\ \        / /  ____|    | |  | |/ __ \ / ____|__   __|
 \ \  /\  / /| |__ ______| |__| | |  | | (___    | |   
  \ \/  \/ / |  __|______|  __  | |  | |\___ \   | |   
   \  /\  /  | |____     | |  | | |__| |____) |  | |   
    \/  \/   |______|    |_|  |_|\____/|_____/   |_|   

 ''')

def check():
if (auth==False):

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

    else: 
        print("Connecting to database")
        print('Database ip :-'+ database_ip)
        print('Database name :-'+ database_name)
        print('Database User :-'+ database_user)
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
        sql="SELECT node_password FROM node_data where node_id =" + node_id
        mycursor.execute(sql)
        Password = mycursor.fetchone()
        if(node_password == Password):
            print ("starting local-host")
            command = 'python requirements.py'
            os.system(command)
        else:
            print("Error Authendication failed")
            check()

    