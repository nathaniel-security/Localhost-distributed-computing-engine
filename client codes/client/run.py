import os
import threading 
  
from get_code_when_free import code_id
sql = "SELECT code_run_command FROM code_data where code_id = " + code_id 
mycursor.execute(sql)
code_run_command = mycursor.fetchone()
command = code_run_command
os.system(command)
