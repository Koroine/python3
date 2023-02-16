import sqlite3
conn=sqlite3.connect('midmorn.db')
conn.execute("INSERT INTO wanafunzi(ID,NAME,AGE,SCHOOL,GENDER)VALUES (1,'DARIUS',21,'eMobibilis','male')")
conn.execute("INSERT INTO wanafunzi(ID,NAME,AGE,SCHOOL,GENDER)VALUES (2,'RAYANN',16,'eMobibilis','female')")
conn.execute("INSERT INTO wanafunzi(ID,NAME,AGE,SCHOOL,GENDER)VALUES (3,'JOHN',18,'eMobibilis','male')")
conn.execute("INSERT INTO wanafunzi(ID,NAME,AGE,SCHOOL,GENDER)VALUES (4,'GRACE',22,'eMobibilis','female')")
conn.execute("INSERT INTO wanafunzi(ID,NAME,AGE,SCHOOL,GENDER)VALUES (5,'DENNIS',24,'eMobibilis','male')")
conn.execute("INSERT INTO wanafunzi(ID,NAME,AGE,SCHOOL,GENDER)VALUES (6,'VALENTINE',17,'eMobibilis','female')")
conn.commit()
print("Records added successfuly")
conn.close()

