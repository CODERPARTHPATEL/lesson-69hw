import sqlite3



conn = sqlite3.connect('database.sqlite')


print('opened database')


#creat a new table in given database with nentioned constraints

conn.execute("""CREATE TABLE CLASS_10111(games i made,how many player they had in a month,year,deleted or not);""")

print('tabe created')

#enter data for 3 diffrent entries
conn.execute("INSERT INTO CLASS_10111(games i made,how many player they have in a month,year,deleted or not)\
VALUES('scorps takeover',1100,'2025',deleted')");


conn.execute("INSERT INTO CLASS_10111(games i made,how many player they have in a month,year,deleted or not)\
VALUES('planet zenac',153,2024'deleted')");

conn.execute("INSERT INTO CLASS_10111(games i made,how many player they have in a month,year,deleted or not)\
VALUES('first game',50,'2023',deleted')");

#save the cahnges
conn.commit()
print('records created')

#display tables
import pandas as pd
tables = pd.read_sql("""SELECT *
                     FROM sqlite_master
                     Where type='table';""",conn)
tables

#read tables
class_10d = pd.read_sql("""SELECT*
                        FROM CLASS_10111;""",conn)

class_10d.head()
