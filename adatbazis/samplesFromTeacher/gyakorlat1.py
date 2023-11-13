import sqlite3
#adatbázis létrehozása, kapcsolódás
conn=sqlite3.connect("utazas.db")
#a változót azért hozzuk létre, hogy legyen egy kurzorunk,
#ahova az sql utasításokat adjuk ki
a=conn.cursor()
#léterhozzuk a felhasználók táblát a zárójelben jelzett mezőkkel és típusokkal
a.execute("CREATE TABLE IF NOT EXISTS utasok(id INTEGER, nev VARCHAR(20), kor INTEGER)")
#lefuttatja az adatok beillesztését, de nem menti
a.execute("INSERT INTO utasok VALUES(4,'Pisti',45)")

#adatok megjelenítése
a.execute("SELECT nev,kor FROM utasok")
adatok=a.fetchall()
print(adatok)

a.execute("SELECT nev,kor FROM utasok WHERE kor>20")
adatok=a.fetchall()
print(adatok)


#adatok frissítése
a.execute("UPDATE utasok SET kor=? WHERE kor=?",(60,45))

a.execute("SELECT nev,kor FROM utasok WHERE kor>20")
adatok=a.fetchall()
print(adatok)

a.execute("DELETE FROM utasok WHERE kor=60")

#ezzel kapcsolatot teremtünk és menti is
conn.commit()
