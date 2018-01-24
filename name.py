first_name = raw_input("Please enter your first name.")
last_name = raw_input("Please enter your last name.")
print "Hello " + first_name + " " + last_name
age = raw_input("Please enter your age.")
age = int(age)
if age >= 18:
   print "Adult"
else:
	print "Child"