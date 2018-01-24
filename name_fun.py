Name = raw_input("Please enter a name.")
len_name = len(Name)
Name = Name.lower()
x = 0
Name_Case = ""

for i in Name:
	if x < 1:
		Name_Case += i.upper()
		x += 1
	else:
		Name_Case += i

print Name_Case


