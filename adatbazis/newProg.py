import tkinter as tk
from tkinter import ttk
from dbManager import *

# ==================================================================
# Globális változók, objektumok, illetve alapvető műveletek
# ==================================================================

db = "metro.db"
root = tk.Tk()
root.title("Adatbázis kezelő v0.2 - Nagy István")
frame = ttk.Frame(root, borderwidth=10, relief="flat", padding=10)
frame.grid()
currentComboboxValue = tk.StringVar()
dbman = DbManager()
dbman.ConnectToDb(db)
table = ttk.Treeview(frame)
iwOpen = False

# ==================================================================

def AppExit():
    dbman.CloseConnectionToDb()
    root.destroy()

def TableColumnNames():
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
    names = TableColumnNames()
    table["columns"] = names
    for name in names:
        table.heading(name, text=name)
    dataList = dbman.curs.fetchall()
    dbman.WriteTableContent(table, dataList)

def ComboboxChanged(event):
    SwitchTable()

def InsertionWindow():
    global iwOpen
    if not iwOpen:
        iwOpen = True
        iw = tk.Toplevel(root)
        iw.title("Rekord hozzáadása")
        iw.protocol("WM_DELETE_WINDOW", lambda: OnIwClose(iw))
        iwf = ttk.Frame(iw, borderwidth=10, relief="flat", padding=10)
        fields = TableColumnNames()
        data = []
        for field in fields:
            ttk.Label(iwf, text=field+":")
            value = tk.StringVar()
            ttk.Entry(iwf, textvariable=value)
            data.append(value)


def OnIwClose(iw:tk.Tk):
    global iwOpen
    iwOpen = False
    iw.destroy()
    
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
# Alap ablak megjelenése, Táblázat indulás utáni feltöltése
# ==================================================================

ttk.Label(frame, text="Fejlesztés alatt...", foreground="#ff0000", font="Arial 18 bold", padding=10).grid(column=0, row=0, columnspan=2)
ttk.Label(frame, text=f"Aktuális adatbázis: {db}", justify="right", font="Arial 12 bold", padding=10).grid(column=0, row=1)
ttk.Button(frame, text="Kilépés", command=AppExit).grid(column=1, row=1)
ttk.Label(frame, text="Tábla:", font="Arial 12 bold", padding=10).grid(column=0, row=2)
combobox.grid(column=1, row=2)
table = ttk.Treeview(frame, columns=TableColumnNames(), show="headings")
table.grid(column=0, columnspan=2, row=3, pady=10)
SwitchTable()

# ==================================================================

# ==================================================================
# Szerkesztő gombok
# ==================================================================

buttonFrame = ttk.Frame(frame, borderwidth=10, relief="solid")
buttonFrame.grid(column=0, columnspan=2, row=4)
buttonFrame.grid()
insert = ttk.Button(buttonFrame, text="Beszúrás", command=InsertionWindow)
insert.grid(column=0, row=0)
edit = ttk.Button(buttonFrame, text="Szerkesztés")
edit.grid(column=1, row=0)
delete = ttk.Button(buttonFrame, text="Törlés")
delete.grid(column=2, row=0)


# ==================================================================


root.protocol("WM_DELETE_WINDOW", AppExit)
root.mainloop()