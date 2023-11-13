from tkinter import *
from tkinter import ttk
from dbManager import *

db = "metro.db"
root = Tk()
root.title("Adatbázis kezelő - Nagy István")

frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Fejlesztés alatt...", foreground="#ff0000", font="Arial 18 bold", padding=10).grid(column=0, row=0)
ttk.Button(frm, text="Kilépés", command=root.destroy).grid(column=1, row=0)
ConnectToDb()
#ttk.Label(frm, text="Tábla neve")
root.mainloop()