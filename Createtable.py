import sqlite3
conn=sqlite3.connect('midmorn.db')
print("Open database successfully")
conn.execute("CREATE TABLE wanafunzi ("
             "ID INT NOT NULL PRIMARY KEY NOT NULL,"
             "NAME TEXT NOT NULL,"
             "AGE INT NOT NULL,"
             "SCHOOL TEXT NOT NULL,"
             "GENDER TEXT NOT NULL)")
print("Table created successfully")
conn.close()
