from server_database_connection import mycursor

while 1:
    mycursor = mydb.cursor()
    mycursor.execute("SELECT code_id FROM process_codes")
    code_id = mycursor.fetchone()


    mycursor.execute("SELECT node_id FROM free_node")
    node = mycursor.fetchone()
    node_id = mycursor.fetchone()


    sql = "INSERT INTO code_node (code_id, node_id) VALUES (%s, %s)"
    val = (code_id,node_id)
    mycursor.execute(sql, val)


