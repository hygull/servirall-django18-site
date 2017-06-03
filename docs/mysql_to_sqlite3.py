# pip install MySql-python

import MySQLdb

db = MySQLdb.connect("localhost", "hygull", "admin@67", "practice_db")

cursor = db.cursor()

cursor.execute("SELECT VERSION()")

data = cursor.fetchone()

print data

cursor.execute("select * from products")

rows = cursor.fetchall()

# sqlite3
import sqlite3

conn = sqlite3.connect("../db.sqlite3")

cursor = conn.execute("SELECT name from sqlite_master where type='table'")

for row in cursor:
	print row

for row in rows[:30]:
	print type(row[0]), type(row[1])
	query = "INSERT INTO HyGoApp_product VALUES("+str(row[0])+", '"+row[1]+"', '"+row[2]+"', "+str(row[3])+", "+str(row[4])+", '"+row[5]+"', '"+row[6]+"')"
	print query
	conn.execute(query)
	conn.commit()

# query="DROP table HyGoApp_product"

# cursor = conn.execute(query)
# conn.commit()
conn.close()
# for row in cursor:
# 	print row[1]

db.close()


