class Student(object):
	def __init__(self, name, address, marks):
		self.name = name
		self.address = address
		self.marks = marks
	def __str__(self):
		return self.name + " lives in " + self.address + " and got " + str(self.marks);

file = open("classfile.txt", "r")

	name1 = file.readline()
	name1 = name1.strip("name: ")
	name1 = name1.strip()

	address1 = file.readline()
	address1 = address1.strip("address: ")
	address1 = address1.strip()

	marks1 = file.readline()
	marks1 = marks1.strip("marks: ")
	marks1 = marks1.strip()
	marks1 = int(marks1)


	student1 = Student(name1, address1, marks1)
	print student1
file.close()