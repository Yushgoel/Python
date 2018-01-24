import easygui, MySQLdb

ctr = 0
rollno = 0
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="",
                     db="pythonspot")


cur = db.cursor()
cur.execute("SELECT * FROM student")

cur1 = cur.fetchall()

for i in cur1:
    if ctr == len(cur1) - 1:
        rollno = i[0] + 1
    ctr += 1

name = ""
marks1 = 0
address1 = ""
fieldValues = []
fieldValues = easygui.multenterbox("Enter the following fields" , fields = ["Name", "marks", "address"])
name = fieldValues[0]
marks1 = fieldValues[1]
address1 = fieldValues[2]

cur.execute("Insert into student(roll_no, full_name, marks, address) Values(%s, %s, %s, %s)" ,  (rollno, name, marks1, address1))
db.commit()

db.close()
