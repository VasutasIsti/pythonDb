import tkinter as tk
from tkinter import ttk
from dbManager import *

db = "metro.db"
root = tk.Tk()
root.title("Adatbázis kezelő v0.2 - Nagy István")
frame = ttk.Frame(root, borderwidth=10, relief="flat", padding=10)
frame.grid()
currentComboboxValue = tk.StringVar()
dbman = DbManager()
dbman.ConnectToDb(db)
table = ttk.Treeview(frame)

def AppExit():
    dbman.CloseConnectionToDb()
    root.destroy()

def FirstTableNames():
    print("Getting table column names")
    comm = "SELECT * FROM " + currentComboboxValue.get()
    data = dbman.curs.execute(comm)
    names = []
    for column in data.description:
        names.append(column[0])
    print("done")
    return list[str](names)

def SwitchTable():
    print("Switching tables")
    global table
    if type(table) is not type(None):
        for i in table.get_children():
            table.delete(i)
    comm = "SELECT * FROM " + currentComboboxValue.get()
    data = dbman.curs.execute(comm)
    names = []
    for column in data.description:
        names.append(column[0])
    table["columns"] = names
    for name in names:
        table.heading(name, text=name)
    dataList = dbman.curs.fetchall()
    dbman.WriteTableContent(table, dataList)

def ComboboxChanged(event):
    SwitchTable()

# ==================================================================
# Dinamikusan feltöltött, adatbázisban megtalálható táblák
# kiválasztására szolgáló Combobox

dbman.curs.execute("SELECT name FROM sqlite_master WHERE type='table';")
tableNames = dbman.curs.fetchall()
combobox = ttk.Combobox(frame, values=tableNames, textvariable=currentComboboxValue, state="readonly")
combobox.current(0)

combobox.bind("<<ComboboxSelected>>", ComboboxChanged)

# ==================================================================

# ==================================================================
# 
# ==================================================================

ttk.Label(frame, text="Fejlesztés alatt...", foreground="#ff0000", font="Arial 18 bold", padding=10).grid(column=0, row=0)
ttk.Button(frame, text="Kilépés", command=AppExit).grid(column=1, row=0)
ttk.Label(frame, text="Tábla:", justify="right", font="Arial 12 bold", padding=10).grid(column=0, row=1)
combobox.grid(column=1, row=1)
table = ttk.Treeview(frame, columns=FirstTableNames(), show="headings")
table.grid(column=0, columnspan=2, row=2, pady=10)
SwitchTable()

# ==================================================================
# Szerkesztő gombok
# ==================================================================

buttonFrame = ttk.Frame(frame, borderwidth=10, relief="solid", padding=10)
buttonFrame.grid(column=0, columnspan=2, row=3)
buttonFrame.grid()
ttk.Button(buttonFrame, text="Beszúrás").grid(column=0, row=0)
ttk.Button(buttonFrame, text="Szerkesztés").grid(column=1, row=0)
ttk.Button(buttonFrame, text="Törlés").grid(column=2, row=0)


# ==================================================================


root.protocol("WM_DELETE_WINDOW", AppExit)
root.mainloop()