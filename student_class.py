class Student(object):
	def __init__(self, name, address, marks):
		self.name = name
		self.address = address
		self.marks = marks
	def __str__(self):
		print self.name + " lives in " + self.address + " and got " + str(self.marks)

file = open("classfile.txt", "w")
for i in range(0, 5):
	name1 = raw_input("Please enter a name ")
	address1 = raw_input("please enter an address ")
	try:
		marks1 = int(raw_input("please enter marks "))
	except ValueError:
		marks1 = raw_input("please enter a number ")
	Student1 = Student(name1, address1, marks1)
	file.write("name: " + Student1.name + "\n")
	file.write("address: " + Student1.address + "\n")
	file.write("marks: " + str(Student1.marks) + "\n")
	file.write("\n")


file.close()