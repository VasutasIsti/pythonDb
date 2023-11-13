import sqlite3

conn=None
curs=None
def adatbazis_letrehozas():
    global conn,curs
    conn=sqlite3.connect("data2.db")
    curs=conn.cursor()
    curs.execute("CREATE TABLE IF NOT EXISTS tanulo(azon varchar(20),nev VARCHAR(20),kor INTEGER,nem VARCHAR (10))")

def adat_beszuras(azon,nev,kor,nem):
    conn=sqlite3.connect("data2.db")
    curs=conn.cursor()
    if not azon.get() or not nev.get() or not kor.get() or nem.get()=='Válassza ki a nemet':
        print('Az összes mező kitöltése kötelező')
        return
    curs.execute("INSERT INTO tanulo VALUES (?,?,?,?)",(azon.get(),nev.get(),kor.get(),nem.get()))
    conn.commit()
    azon.delete(0,'end')
    nev.delete(0,'end')
    kor.delete(0,'end')

def adat_kiiras(table):
    conn=sqlite3.connect("data2.db")
    curs=conn.cursor()
    curs.execute("SELECT * FROM tanulo")
    adatok=curs.fetchall()
    table.delete(*table.get_children())
    
    for adat in adatok:
        table.insert("","end",values=(adat[0],adat[1],adat[2],adat[3]))
def adat_export():
    conn=sqlite3.connect("data2.db")
    curs=conn.cursor()
    curs.execute("SELECT * FROM tanulo")
    adatok=curs.fetchall()
    with open("kimenet.csv","w",encoding="utf-8") as f:
        f.write(";".join(["azonosító","név","életkor","nem"]))
        f.write("\n")
        for adat in adatok:
            f.write(";".join(str(d)for d in adat))
            f.write("\n")
    f.close()
def adatbazis_lezaras():
    if conn and curs:
        curs.close()
        conn.close()















        
