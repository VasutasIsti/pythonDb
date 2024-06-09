# ==================================================================
# Felhasznált modulok importálása
# ==================================================================
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from dbManager import *
# ==================================================================

# ==================================================================
# Globális változók, objektumok, illetve alapvető műveletek
# ==================================================================
db = filedialog.askopenfilename()
root = tk.Tk()
root.update()

root.deiconify()
root.lift()
root.title("Adatbázis kezelő v0.3 - Nagy István")
root.resizable(0, 0)                                                    # Amíg nem találok megoldást a treeview dinamikus méretezésére, 
                                                                        # addig nem lehet az ablak méretét állítani.
frame = ttk.Frame(root, borderwidth=10, relief="flat", padding=10)
frame.grid(row=0, column=0, sticky="news")
currentComboboxValue = tk.StringVar()
dbman = DbManager()
dbman.ConnectToDb(db)
treeview = ttk.Treeview(frame)
topOpen = False
# ==================================================================

def OnAppExit():                                                        # Alkalmazás bezárásának egyedi folyamata.
    """Closes database connection and exits the application."""
    dbman.CloseConnectionToDb()
    root.destroy()

def OnConfigure(event):                                                 # TODO! Treeview méretezése az ablak méretezésével együtt.
    treeview.update_idletasks()
    verticalScrollbar.set(0, 1)

def SwitchTable():                                                      # Tábla lecserélése, valamint új tartalom kiíratása
    print("Switching tables")
    global treeview
    if type(treeview) is not type(None):
        for i in treeview.get_children():
            treeview.delete(i)
    names = dbman.GetTableColumnNames(currentComboboxValue.get())
    treeview["columns"] = names
    for name in names:
        treeview.heading(name, text=name)
    dataList = dbman.curs.fetchall()
    print("fetch done")
    dbman.WriteTableContent(treeview, dataList)

def OnComboboxChange(event):                                            # Segéd függvény a SwitchTable() meghívásához
    SwitchTable()

def OnIwEntryChange(fields:list, data:list, result:tk.StringVar):       # TODO! Dinamikus parancs kiírás Entry-k szerkesztésekor.
#### Még nincs befejezve. 
    command = "INSERT INTO " + currentComboboxValue.get() + "("
    for field in fields:
        command += str(field) + ", "
    
    command = command[:len(command) - 2]
    command += ") VALUES ("
    for i in range(len(data)):
        if data[i] == type(None):
            break
        else:
            command += str(data[i].get()) + ", "
    
    command = command[:len(command) - 2]
    command += ");"
    result.set(command)

def OnIwClose(iw:tk.Toplevel):                                          # Beszúrási ablak bezárásának egyedi folyamata.
    global topOpen
    topOpen = False
    combobox.state(["!disabled"])
    iw.destroy()

def OnIwInsert(iw:tk.Toplevel, fields:list, data:list, tableName:str):  # A Beszúr gomb megnyomásakor lezajló folyamatok.
    dbman.InsertRecord(dbman.CreateInsertionCommand(fields, data, tableName))
    SwitchTable()
    OnIwClose(iw)

def InsertionWindow():                                                  # A Beszúrás gomb megnyomásakor lezajló folyamatok.
    global topOpen
    if not topOpen:
        topOpen = True
        combobox.state(["disabled"])
        iw = tk.Toplevel(root)
        iw.title("Rekord hozzáadása")
        iw.protocol("WM_DELETE_WINDOW", lambda: OnIwClose(iw))
        iwf = ttk.Frame(iw, borderwidth=10, relief="flat", padding=10)
        iwf.grid()
        fields = dbman.GetTableColumnNames(currentComboboxValue.get())
        dataN = 0
        data = []
        # print(data)
        # resultValue = tk.StringVar()              # Amíg bugos a további része, addig nem hozom létre.
        for x in range(len(fields)):
            ttk.Label(iwf, text=fields[x]+":").grid(column=0, row=x)
            value = tk.StringVar()
            ttk.Entry(iwf, textvariable=value).grid(column=1, row=x)
            data.append(value)
            dataN += 1
        
        ttk.Button(iwf, text="Beszúr", command=lambda: OnIwInsert(iw, fields, data, currentComboboxValue.get())).grid(column=0, columnspan=2, row=dataN)

        #### Egyszer majd ez lesz egy folyamatosan frissülő parancs kiírás, mint a DB Browser-ben. Még egyenlőre buggos
        # for x in range(len(data)):
        #     if data[x] is not type(None):
        #         data[x].trace("w", lambda name, index, mode, value=value: OnIwEntryChange(fields, data, resultValue))
        # result = ttk.Entry(iwf, textvariable=resultValue, width=100)
        # result.state(["readonly"])
        # result.grid(column=0, columnspan=6, row=datas)

def OnDwClose(dw:tk.Toplevel):                                          # Törlési ablak bezárásának egyedi folyamata.
    global topOpen
    topOpen = False
    combobox.state(["!disabled"])
    dw.destroy()

def OnDwDelete(dw:tk.Toplevel, tableName:str, columnName, value):       # A Törlés gomb megnyomásakor lezajló folyamatok.
    dbman.RemoveRecord(dbman.CreateDeletionCommand(columnName, value, tableName))
    SwitchTable()
    OnDwClose(dw)

def DeletionWindow():                                                   # A Törlés gomb megnyomásakor lezajló folyamatok.
    global topOpen
    if not topOpen:
        topOpen = True
        combobox.state(["disabled"])
        dw = tk.Toplevel(root)
        dw.title("Rekord Törlése")
        dw.protocol("WM_DELETE_WINDOW", lambda: OnDwClose(dw))
        dwf = ttk.Frame(dw, borderwidth=10, relief="flat", padding=10)
        dwf.grid()
        ttk.Label(dwf, text="Elsődleges kulcs mezőneve:").grid(column=0, row=0)
        columnName = tk.StringVar()
        ttk.Entry(dwf, textvariable=columnName).grid(column=1, row=0)
        ttk.Label(dwf, text="Elsődleges kulcs értéke:").grid(column=0, row=1)
        value = tk.StringVar()
        ttk.Entry(dwf, textvariable=value).grid(column=1, row=1)
        ttk.Button(dwf, text="Törlés", command=lambda: OnDwDelete(dw, currentComboboxValue.get(), columnName.get(), value.get())).grid(column=0, columnspan=2, row=2)

# ==================================================================
# Dinamikusan feltöltött, adatbázisban megtalálható táblák
# kiválasztására szolgáló Combobox
# ==================================================================
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
style = ttk.Style()
style.theme_use("clam")
treeview = ttk.Treeview(frame, columns=dbman.GetTableColumnNames(currentComboboxValue.get()), show="headings")
treeview.grid(column=0, columnspan=2, row=3, pady=10, sticky="news")
verticalScrollbar = ttk.Scrollbar(frame, orient="vertical", command=treeview.yview, style="Vertical.TScrollbar")
verticalScrollbar.grid(column=2, row=3, sticky="news", pady=10)
treeview.configure(yscrollcommand=verticalScrollbar.set)
treeview.bind("<Configure>", OnConfigure)
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
edit.state(["disabled"])
edit.grid(column=1, row=0)
delete = ttk.Button(buttonFrame, text="Törlés", command=DeletionWindow)
delete.grid(column=2, row=0)
# ==================================================================

root.protocol("WM_DELETE_WINDOW", OnAppExit)
root.mainloop()