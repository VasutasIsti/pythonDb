from tkinter import *
from tkinter import ttk
from db_manager import *
adatbazis_letrehozas()
a=Tk()
a.title('Adatbázisos példa')
a.geometry('1020x640')
a.resizable(False,False)
Label(a,text='Id',font="Helvetica 12 bold").grid(row=0,column=0)
azon=Entry(a,font="helvetica 20 bold")
azon.grid(row=0,column=1,padx=5,pady=5)

Label(a,text='Név',font="Helvetica 12 bold").grid(row=1,column=0)
nev=Entry(a,font="helvetica 20 bold")
nev.grid(row=1,column=1,padx=5,pady=5)

Label(a,text='Kor',font="Helvetica 12 bold").grid(row=2,column=0)
kor=Entry(a,font="helvetica 20 bold")
kor.grid(row=2,column=1,padx=5,pady=5)

Label(a,text='Neme',font="Helvetica 12 bold").grid(row=3,column=0)
nem=StringVar(a)
nem.set('Válassza ki a nemet')
neme=OptionMenu(a,nem,"férfi","nő")
neme.grid(row=3,column=1,padx=5,pady=5)


Button(a,text='Adatbevitel',command=lambda:adat_beszuras(azon,nev,kor,nem),font='Helvetica 12 bold').grid(row=4,column=0,columnspan=2,padx=5,pady=5)
mezok=('id','név','kor','nem')
table=ttk.Treeview(a,columns=mezok,show="headings")
for col in mezok:
    table.heading(col,text=col)
table.grid(row=5,column=0,columnspan=2,padx=5,pady=5)
Button(a,text='adatok lekérdezése',command=lambda: adat_kiiras(table),font='Helvetica 12 bold').grid(row=6,column=0,columnspan=2,padx=5,pady=5)
Button(a,text='adatok mentése',command=adat_export,font='Helvetica 12 bold').grid(row=7,column=0,columnspan=2,padx=5,pady=5)
adatbazis_lezaras()

a.mainloop()
