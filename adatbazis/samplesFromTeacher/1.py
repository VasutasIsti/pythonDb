import sqlite3
from pprint import pprint
#adatbázis létrehozása, kapcsolódás
conn=sqlite3.connect("adatbazis.db")
#a változót azért hozzuk létre, hogy legyen egy kurzorunk,
#ahova az sql utasításokat adjuk ki
a=conn.cursor()
#léterhozzuk a felhasználók táblát a zárójelben jelzett mezőkkel és típusokkal
a.execute("CREATE TABLE IF NOT EXISTS felhasznalok(nev TEXT, kor INTEGER, nem TEXT, pontszam REAL)")
#lefuttatja az adatok beillesztését, de nem menti
a.execute("INSERT INTO felhasznalok VALUES('Péter',17,'férfi',8)")
#ezzel kapcsolatot teremtünk és menti is

#adatok megjelenítése
a.execute("SELECT * FROM felhasznalok")
adatok=a.fetchall()
print(adatok)
#adatok frissítése
a.execute("UPDATE felhasznalok SET nem=? WHERE nem=?",('hölgy','nő'))

a.execute("DELETE FROM felhasznalok WHERE nev='Péter'")
conn.commit()
conn.close()
