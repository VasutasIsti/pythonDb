import tkinter as tk
from tkinter import ttk
from dbManager import *

db = "metro.db"
root = tk.Tk()
root.title("Adatbázis kezelő - Nagy István")
conn = None
curs = None
table = None

dbman = DbManager(conn, curs)
dbman.ConnectToDb(db)

def AppExit(root):
    dbman.CloseConnectionToDb()
    root.destroy()

# ConnectToDb(db, conn, curs)

def TableChange(event):
    print("Changed!")
    dbman.WriteTableContent(root, ttk, table, Current_tableName.get())

frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Fejlesztés alatt...", foreground="#ff0000", font="Arial 18 bold", padding=10).grid(column=0, row=0)
ttk.Label(frm, text="Tábla: ", font="Arial 12 bold", padding=10, ).grid(column=0, row=1)

dbman.curs.execute("SELECT name FROM sqlite_master WHERE type='table';")
tableNames = dbman.curs.fetchall()
Current_tableName = tk.StringVar()
combobox = ttk.Combobox(frm, textvariable=Current_tableName)
combobox["values"] = tableNames
combobox.current(0)

combobox.bind("<<ComboboxSelected>>", TableChange)
combobox.grid(column=1, row=1)
print(Current_tableName)
dbman.WriteTableContent(root, ttk, table, Current_tableName.get())


ttk.Button(frm, text="Kilépés", command=lambda: AppExit(root)).grid(column=1, row=0)

# ttk.Label(frm, text="Tábla neve")
root.mainloop()