# sqlite3
import sqlite3

conn = sqlite3.connect("../db.sqlite3")
conn2 = sqlite3.connect("../db.sqlite32")

cursor = conn2.execute("SELECT * from HyGoApp_product")

# for row in cursor:
# 	print row

for row in cursor:
	query = "INSERT INTO HyGoApp_product VALUES("+str(row[0])+", '"+row[1]+"', '"+row[2]+"', "+str(row[3])+", "+str(row[4])+", '"+row[5]+"', '"+row[6]+"')"
	print query
	conn.execute(query)
	conn.commit()

# query="DROP table HyGoApp_product"

# cursor = conn.execute(query)
# conn.commit()
conn.close()
conn2.close()
# for row in cursor:
# 	print row[1]

db.close()


