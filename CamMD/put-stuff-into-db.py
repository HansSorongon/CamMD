import sqlite3
connect = sqlite3.connect('CamMD.db')
cursor = connect.cursor()

#create table for database

cursor.execute("""CREATE TABLE IF NOT EXISTS CamMD2(
   wound TEXT NOT NULL,
   step1 TEXT NOT NULL,
   step2 TEXT NOT NULL
   )""")
connect.commit()

wound="BLISTER"
step1 = """DO NOT POP THE BLISTER: Popping the blister will create a open wound which will be open to infection. A popped blister will be exposed to bacteria."""
step2 = """SOAK IN WARM WATER: Soaking the blister in warm water will allow the blister to soften and soothe your pain. Make sure to use a clean bowl filled 
warm water and soak the blister for 15 minutes. Pat it dry with a clean towel afterwards."""

cursor.execute("INSERT INTO CamMD2 ( wound  , step1, step2) VALUES (?,?,?)", (wound,step1,step2))
connect.commit()
print("done")