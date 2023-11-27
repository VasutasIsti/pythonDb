# This was planned to be used to create tables for this project.
# It was made obsolate

from dbManager import *

db = "./databases/metro.db"
ConnectToDb(db)
CreateTable("dolgozo", [["id", "int(11)", "NOT NULL"],
                        ["nev", "text", "NOT NULL"],
                        ["vezetoi", "date", "DEFAULT NULL"],
                        ["segedvezetoi", "date", "DEFAULT NULL"]])
CreateTable("forda", [["id", "int(11)", "NOT NULL"],
                      ["kezdoido", "time", "NOT NULL"],
                      ["kezdoall", "int(11)", "NOT NULL"],
                      ["vegzoido", "time", "NOT NULL"],
                      ["vegzoall", "int(11)", "NOT NULL"]])
#CreateTable("allomas", [["id", "int(11)", "NOT NULL"],
#                        ["nev", "text", "NOT NULL"]])
#CreateTable("kocsi", [["id", "int(11)", "NOT NULL"],
#                       ["tipus", "text", "NOT NULL"],
#                       []])
# CreateTable("menetrend" [[]])
# CreateTable("muhely", [[]])
# CreateTable("szerelveny" [[]])

CloseConnectionToDb()
