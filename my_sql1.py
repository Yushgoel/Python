import MySQLdb

db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="",
                     db="pythonspot")
ctr = 1
cur = db.cursor()
cur.execute("SELECT * FROM student where roll_no > 1 ")
for row in cur.fetchall() :
#    if ctr == len(row):
#	   	break;
	print row
db.close()
