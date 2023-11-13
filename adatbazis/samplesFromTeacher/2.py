from tkinter import *
from tkinter import ttk
win=Tk()
win.title('Adatbázisos példa')
win.geometry('1020x640')
win.resizable(False,False)
Label(win,text='Név',font="Helvetica 12 bold").grid(row=0,column=0)
name=Entry(win,font="helvetica 20 bold")
name.grid(row=0,column=1,padx=5,pady=5)

Label(win,text='Kor',font="Helvetica 12 bold").grid(row=1,column=0)
age=Entry(win,font="helvetica 20 bold")
age.grid(row=1,column=1,padx=5,pady=5)

Label(win,text='Neme',font="Helvetica 12 bold").grid(row=2,column=0)
gender=StringVar(win)
gender.set('select your gender')
genders=OptionMenu(win,gender,"male","female")
genders.grid(row=2,column=1,padx=5,pady=5)

Label(win,text='Pontszám',font="Helvetica 12 bold").grid(row=3,column=0)
pontszam=Entry(win,font="helvetica 20 bold")
pontszam.grid(row=3,column=1,padx=5,pady=5)
Button(win,text='Adatbevitel',font='Helvetica 12 bold').grid(row=4,column=0,columnspan=2,padx=5,pady=5)
mezok=('id','név','kor','nem','pontszám')
table=ttk.Treeview(win,columns=mezok,show="headings")
for col in mezok:
    table.heading(col,text=col)
table.grid(row=5,column=0,columnspan=2,padx=5,pady=5)
Button(win,text='adatok lekérdezése',font='Helvetica 12 bold').grid(row=6,column=0,columnspan=2,padx=5,pady=5)
Button(win,text='adatok mentése',font='Helvetica 12 bold').grid(row=7,column=0,columnspan=2,padx=5,pady=5)
win.mainloop()
