import sqlite3

class DbManager:
    def __init__(self, conn, curs):
        self.conn = conn
        self.curs = curs

    def ConnectToDb(self, db:str):
        """Connects to the defined database. There can be only one open database connection at a time."""
        self.conn = sqlite3.connect(db)
        self.curs = self.conn.cursor()
        print("Database connection estabilished.")

    def CloseConnectionToDb(self):
        """Closes connection to the used database."""
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
        
    def WriteTableContent(self, root, ttk, table, dbTable:str):
        """Writes table content of the specified table. It only works on tables, which column count is between 2 and 10."""
        
        comm = "SELECT * FROM " + dbTable
        data = self.curs.execute(comm)
        
        # data=cursor.execute('''SELECT * FROM table_name''')

        names = []

        for column in data.description:
            names.append(column[0])
        
        table = ttk.Treeview(root, columns=names, show="headings")
        table.grid(column=0, columnspan=2, row=2)
        
        for col in names:
            table.heading(col, text=col)

        print("exec done")
        dataList = self.curs.fetchall()
        print("fetch done")
        table.delete(*table.get_children())
        root.update()
        root.update_idletasks()
        for data in dataList:
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
                case default:
                    print("HIBA! Túl nagy adatbázis rekord.")
