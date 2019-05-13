from database import *



while True:
    sql = "SELECT node_id FROM free_node"
    mycursor.execute(sql)
    myresult = mycursor.fetchone()
    for x in myresult:
        print(x)

    node_id = x

    print(node_id)


    # now delete node from free node

    query = "DELETE FROM free_node WHERE node_id = " + node_id + " "
    print(query)
    # data
    #data = (node_id,)

    # execute
    mycursor.execute(query)

    # commit
    mydb.commit()






    sql = "SELECT code_name FROM code"
    mycursor.execute(sql)
    myresult = mycursor.fetchone()
    for x in myresult:
        print(x)

    code_name = x

    print(code_name)



    query = "DELETE FROM code WHERE code_name = " + code_name + " "
    print(query)
    # data
    #data = (node_id,)

    # execute
    mycursor.execute(query)

    # commit
    mydb.commit()







    node_id = str(node_id)
    code_name = str(code_name)

    
    mycursor = mydb.cursor()
    sql = "INSERT INTO node_code (node_id,code_name) VALUES (%s,%s)"
    val = (node_id,code_name,)
    mycursor.execute(sql, val)
    
    mydb.commit()                 

    #
    #
    #
    #sql = "INSERT INTO node_code (code_name,node_id) VALUES (%s,%s)"
    #val = (code_name,node_id)
    #mycursor.execute(sql, val)
    #
    #mydb.commit()          
    #


