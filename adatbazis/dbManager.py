import sqlite3

conn = None
curs = None

def ConnectToDb(db:str):
    global conn, curs
    conn = sqlite3.connect(db)
    curs = conn.cursor()

def CloseConnectionToDb():
    if conn and curs:
        curs.close()
        conn.close()

def CreateTable(tableName, fields):
    command = "CREATE TABLE IF NOT EXISTS" + tableName + "("
    for x in fields:
        command += x[0]
        command += " " + x[1]
        index = 2
        while x[index]:
            command += " " + x[index]
            index += 1
        command += ", "
    command = command[:-2]
    command += ")"
    print(command)
    
