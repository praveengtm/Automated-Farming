import sqlite3

conn = sqlite3.connect('sensor.db')

c = conn.cursor()

c.execute("""CREATE TABLE sensors(
            temp integer,
            hum integer)""")

conn.commit()
