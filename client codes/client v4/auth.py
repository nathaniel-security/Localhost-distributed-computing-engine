import os
import mysql.connector
import ftplib as f
import getpass
import ftplib
import json
#function

def hello():
    os.system('cls')
    print('''
888       888 8888888888      888    888  .d88888b.   .d8888b. 88888888888 
888   o   888 888             888    888 d88P" "Y88b d88P  Y88b    888     
888  d8b  888 888             888    888 888     888 Y88b.         888     
888 d888b 888 8888888         8888888888 888     888  "Y888b.      888     
888d88888b888 888             888    888 888     888     "Y88b.    888     
88888P Y88888 888      888888 888    888 888     888       "888    888     
8888P   Y8888 888             888    888 Y88b. .d88P Y88b  d88P    888     
888P     Y888 8888888888      888    888  "Y88888P"   "Y8888P"     888     

    ''')



def auth():

    node_id = input("Node ID:- ")#'123'
    node_password = getpass.getpass(prompt=' Node Password:- ', stream=None)#'456'#
    database_ip = input('Database ip:- ')#'localhost'#
    database_user = input('Database user:- ')#'root'
    database_password =getpass.getpass(prompt=' Database Password:- ', stream=None)# ''#
    database_name = input("Database name:- ")#'we_host_data'#
    ftp_ip = input("FTP IP :-")#'192.168.43.91'#
    ftp_user= input("FTP User :-")#'root'#
    ftp_password = getpass.getpass(prompt=' Ftp Password:- ', stream=None)#''#

    print(node_id)
    print(node_password)
    print(database_ip)
    print(database_name)
    print(database_password)
    print(database_user)
    print(ftp_ip)
    print(ftp_user)
    print(ftp_password)
   

    #database
    try:

        mydb = mysql.connector.connect(
          host=database_ip,
          user=database_user,
          passwd=database_password,
          database=database_name
        )

        mycursor = mydb.cursor()
        print(mydb)
        print("\n\nDatabase connection successfull\n\n")
    except Exception as error:
        print("Error :- ",error)
        print('\n\ndatabase connetion problem\n\n')

    #ftp connection
    try:
        #ftp = f.FTP(ftp_ip)
        
        ftp = ftplib.FTP(ftp_ip)
        ftp.login(ftp_user, ftp_password)
        print('\n\n FTP connetion successfull\n\n')

 
    except Exception as error:
        print("Error :- ",error)
        print('\n\FTP connetion problem\n\n')
   
    #node checking
    try:
        node_id= str(node_id)
        node_password = str(node_password)
        sql = "SELECT node_id FROM node_data where node_id = '"+node_id +"' AND node_password = '"+node_password + "'"
        mycursor.execute(sql)
        myresult = mycursor.fetchone()
        for x in myresult:
            if(x==node_id):
                print("\n\nWelcome\n\n")
                print("\n\n Storing your data locally so that you dont need to borther in furute don't worry you can change your information in future...\n\n")
                    
            else:
                print("\n\nWrong Credentials")
                exit()


    except Exception as error:
        print("\n\nError :- ",error)
        print('\n\n node problem\n\n')
   

    #writting into json file
    data = {} 
    data['config'] = []  
    data['config'].append({  
    'node id': node_id,
    'node password': node_password,
    'database ip': database_ip,
    'database user': database_user,
    'database name': database_name,
    'database password': database_password,
    'ftp ip':ftp_ip,
    'ftp user': ftp_user,
    'ftp password' : ftp_password
    })
    

    print('\n\nwritting data into json file\n\n')
    with open('config.json', 'w') as outfile:  
        json.dump(data, outfile)

    print('\n\nJson file made\n\n')
           

    os.system('python requirements.py')



hello()
auth()