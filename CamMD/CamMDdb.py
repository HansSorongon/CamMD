import sqlite3
connect = sqlite3.connect('CamMD.db')
cursor = connect.cursor()

def find_wound(disease):
    """Find the wound in database and then return the steps"""

    cursor.execute("SELECT step1,step2 FROM CamMD2 WHERE wound = ?", (disease,))
    recommendation=cursor.fetchone()
    step1 = recommendation[0]
    step2 = recommendation[1]
    return step1, step2