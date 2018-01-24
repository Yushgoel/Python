import easygui
file = open("classfile.txt", "w")
option = True
class Student(object):
	"""docstring for Student"""
	def __init__(self, name, address, marks, counter):
		self.name = name
		self.address = address
		self.marks = marks
		self.counter = counter
	def write_file(self):
		
		if self.counter == 0:
			file.write("Name: " + self.name + "\n")
			self.counter += 1
		if self.counter == 1:
			file.write("Address: " + self.address + "\n")
			self.counter += 1
		if self.counter == 2:
			file.write("Marks: " + self.marks + "\n")		
		
while option == True:
	ctr = 0
	msg = "Enter student's information"
	title = "Student info"
	fieldNames = ["Name","Address","Marks"]
	fieldValues = []  # we start with blanks for the values
	fieldValues = easygui.multenterbox(msg,title, fieldNames)
	if len(fieldValues[0]) < 3:
		fieldValues[0] = easygui.textbox("Please enter a proper name ")
	if fieldValues[2] < 0 or fieldValues[2] > 100:
		fieldValues[2] = easygui.textbox("Please enter marks within 0 to 100 ")
	student1 = Student(fieldValues[0], fieldValues[1], fieldValues[2], ctr)
	easygui.msgbox(fieldValues)
	student1.write_file()
	option = easygui.ynbox("Add another student")

file.close()