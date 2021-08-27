import sqlite3
connect = sqlite3.connect('CamMD.db')
cursor = connect.cursor()

#create table for database

cursor.execute("""CREATE TABLE IF NOT EXISTS CamMD(
   #wound TEXT NOT NULL,
   #recommendation TEXT NOT NULL
   #)""")
#connect.commit()
wound="rashes"
recommendation=""" """

cursor.execute("INSERT INTO CamMD ( wound  , recommendation) VALUES (?,?)", (wound,recommendation))
connect.commit()