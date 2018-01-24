import MySQLdb

db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="",
                     db="pythonspot")
ctr = 1
cur = db.cursor()
cur.execute("DELETE  FROM student where roll_no = 7 ")
db.commit()

db.close()
