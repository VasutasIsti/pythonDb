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
treeview = ttk.Treeview(frame)
iwOpen = False

# ==================================================================

def OnAppExit():
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
    global treeview
    if type(treeview) is not type(None):
        for i in treeview.get_children():
            treeview.delete(i)
    names = TableColumnNames()
    treeview["columns"] = names
    for name in names:
        treeview.heading(name, text=name)
    dataList = dbman.curs.fetchall()
    dbman.WriteTableContent(treeview, dataList)

def OnComboboxChange(event):
    SwitchTable()

def OnIwEntryChange(fields:list, data:list, result:tk.StringVar):
    """Not yet working."""
    command = "INSERT INTO ("
    for field in fields:
        command += str(field) + " ,"
    
    command += ") VALUES ("
    for i in range(len(data)):
        if data[i][1] == type(None):
            break
        else:
            command += str(data[i][1].get) + " ,"
    
    command += ");"
    result.set(command)

def CreateInsertionCommand(fields:list, data:list, tableName:str):
    for i in range(len(data)):
        if data[i][1].get() == "":
            print(f"Hiányzó adat ({fields[i]})")
            return
    command = "INSERT INTO " + tableName + " ("
    for field in fields:
        command += str(field) + ", "

    command = command[:len(command) - 2]
    command += ") VALUES ("
    for i in range(len(data)):
        if data[i][1] == type(None):
            break
        else:
            command += str(data[i][1].get()) + ", "

    command = command[:len(command) - 2]
    command += ");"
    print(f"Command: {command}")
    return command

def OnIwClose(iw:tk.Tk):
    global iwOpen
    iwOpen = False
    iw.destroy()
            
def InsertionWindow():
    global iwOpen
    if not iwOpen:
        iwOpen = True
        iw = tk.Toplevel(root)
        iw.title("Rekord hozzáadása")
        iw.protocol("WM_DELETE_WINDOW", lambda: OnIwClose(iw))
        iwf = ttk.Frame(iw, borderwidth=10, relief="flat", padding=10)
        iwf.grid()
        fields = TableColumnNames()
        dataN = 0
        data = []
        # print(data)
        # resultValue = tk.StringVar()
        for x in range(len(fields)):
            label = ttk.Label(iwf, text=fields[x]+":")
            label.grid(column=0, row=x)
            value = tk.StringVar()
            entry = ttk.Entry(iwf, textvariable=value)
            entry.grid(column=1, row=x)
            data.append([label, value, entry])
            dataN += 1
        
        ttk.Button(iwf, text="Beszúr", command=lambda: dbman.InsertRecord(CreateInsertionCommand(fields, data, currentComboboxValue.get()))).grid(column=0, row=dataN)
        # for x in range(len(data)):
        #     if data[x] is not type(None):
        #         data[x][1].trace("w", lambda name, index, mode, value=value: OnIwEntryChange(fields, data, resultValue))
        # result = ttk.Entry(iwf, textvariable=resultValue, width=100)
        # result.state(["readonly"])
        # result.grid(column=0, columnspan=6, row=datas)

    
# ==================================================================
# Dinamikusan feltöltött, adatbázisban megtalálható táblák
# kiválasztására szolgáló Combobox

dbman.curs.execute("SELECT name FROM sqlite_master WHERE type='table';")
tableNames = dbman.curs.fetchall()
combobox = ttk.Combobox(frame, values=tableNames, textvariable=currentComboboxValue, state="readonly")
combobox.current(0)
combobox.bind("<<ComboboxSelected>>", OnComboboxChange)

# ==================================================================

# ==================================================================
# Alap ablak megjelenése, Táblázat indulás utáni feltöltése
# ==================================================================

ttk.Label(frame, text="Fejlesztés alatt...", foreground="#ff0000", font="Arial 18 bold", padding=10).grid(column=0, row=0, columnspan=2)
ttk.Label(frame, text=f"Aktuális adatbázis: {db}", justify="right", font="Arial 12 bold", padding=10).grid(column=0, row=1)
ttk.Button(frame, text="Kilépés", command=OnAppExit).grid(column=1, row=1)
ttk.Label(frame, text="Tábla:", font="Arial 12 bold", padding=10).grid(column=0, row=2)
combobox.grid(column=1, row=2)
treeview = ttk.Treeview(frame, columns=TableColumnNames(), show="headings")
treeview.grid(column=0, columnspan=2, row=3, pady=10)
SwitchTable()

# ================W==================================================

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


root.protocol("WM_DELETE_WINDOW", OnAppExit)
root.mainloop()