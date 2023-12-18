import sqlite3

class DbManager:
    def __init__(self, conn:sqlite3.Connection=None, curs:sqlite3.Connection.cursor=None):
        self.conn = conn
        self.curs = curs

    def ConnectToDb(self, db:str):
        """Connects to the defined database. There can be only one open database connection at a time."""
        self.conn = sqlite3.connect(db)
        self.curs = self.conn.cursor()
        print("Database connection estabilished.")

    def CloseConnectionToDb(self):
        """Closes connection to the used database."""
        self.conn.commit()
        self.curs.close()
        self.conn.close()
        print("Database connection closed.")

    def CreateTable(self, tableName:str, fields:list):
        """Creates a table with specified name and columns.
        In the fields list, an entry must contain at least the name and the type of the column.
        You can add more arguments to a record if necessary"""
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
        command += ") DEFAULT CHARSET=utf8 COLLATE=utf8_hungarian_ci"
        print(command)

    def TableColumnNames(self, tableName:str):
        """Returns column names of the "tableName" table, as a list of strings."""
        print("Getting table column names")
        comm = "SELECT * FROM " + tableName
        data = self.curs.execute(comm)
        names = []
        for column in data.description:
            names.append(column[0])
        print("done")
        return list[str](names)

    def CreateInsertionCommand(self, fields:list, data:list, tableName:str):
        """Returns the INSERT INTO statement from field names and their respective value"""
        for i in range(len(data)):
            if data[i].get() == "":
                print(f"Hiányzó adat ({fields[i]})")
                return
        command = f"INSERT INTO {tableName} ("
        for field in fields:
            command += str(field) + ", "

        command = command[:len(command) - 2]
        command += ") VALUES ("
        for i in range(len(data)):
            if data[i] == type(None):
                break
            else:
                try:
                    number = int(data[i].get())
                    command += f"{number}, "
                except ValueError:
                    command += f"\"{data[i].get()}\", "

        command = command[:len(command) - 2]
        command += ");"
        print(f"Command: {command}")
        return command

    def InsertRecord(self, command:str):
        self.curs.execute(command)

    def CreateDeletionCommand(self, idColumnName:str, id:str, tableName:str):
        command = f"DELETE FROM {tableName} WHERE {idColumnName}={id};"
        return command

    def RemoveRecord(self, command:str):
        self.curs.execute(command)
        
    def WriteTableContent(self, table, dataList):
        """Writes table content of the specified table. It only works on tables, which column count is between 2 and 10."""
        
        print("fetch done")
        
        for data in dataList:
            #### Not the most beautiful, but it works... until 10 entries :)
            match(len(data)):
                case 1:
                    print("HIBA! Túl kicsi adatbázis.")
                case 2:
                    table.insert("", "end", values=(data[0], data[1]))
                case 3:
                    table.insert("", "end", values=(data[0], data[1], data[2]))
                case 4:
                    table.insert("", "end", values=(data[0], data[1], data[2], data[3]))
                case 5:
                    table.insert("", "end", values=(data[0], data[1], data[2], data[3], data[4]))
                case 6:
                    table.insert("", "end", values=(data[0], data[1], data[2], data[3], data[4], data[5]))
                case 7:
                    table.insert("", "end", values=(data[0], data[1], data[2], data[3], data[4], data[5], data[6]))
                case 8:
                    table.insert("", "end", values=(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7]))
                case 9:
                    table.insert("", "end", values=(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8]))
                case 10:
                    table.insert("", "end", values=(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9]))
                case _:
                    print("HIBA! Túl nagy adatbázis rekord.")
