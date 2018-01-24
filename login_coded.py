import easygui

password = ""
username = " "
option = easygui.buttonbox("Sign up or login" ,choices = ["Sign up", "Login", "Forgot Password"])
breakornot = False
if option == "Forgot Password":
	user = easygui.textbox("Please enter username ")
	f = open("login.txt", "r")
	user = user.lower()
	printer = ""
	p1 = []
	while len(username) != 0:
		username = f.readline()
		username = username.strip()
		username = username.lower()
		if user == username:
			password = f.readline()
			password = password.strip()
			for i in password:
				if i == " ":
					printer = printer + chr(int("".join(p1)))
				else:
					p1.append(i)
	easygui.msgbox(printer)
	print printer
else:
	fielValues = []
	Fields = ["Username", "Password"]
	msg = "Enter username and password to login"
	title = "Login/Signup"
	fielValues = easygui.multpasswordbox(msg,title,Fields)

	l1 = []
	for i in fielValues[1]:
		l1.append(bin(ord(i)))
	fielValues[1] = " ".join(l1)

	if option == "Sign up":
		f = open("login.txt", "r")
		while len(username) != 0:
			username = f.readline()
			username = username.strip()
			username = username.lower()
			if fielValues[0].lower() == username:
				fielValues[0] = easygui.msgbox("Please enter unique username ")
				breakornot = True
		if breakornot == False:
			f = open("login.txt", "a+")
			
			f.write(fielValues[0] + "\n")

			f.write(fielValues[1] + "\n")
			breakornot = True

	elif option == "Login":
		f = open("login.txt", "r")
		username = f.readline()
		username = username.strip()
		username = username.lower()
		#print "line = ///%s///" % username
		password = f.readline()
		password = password.strip()
		print password
		

		#print "line = ///%s///" % password
	while len(username) != 0:
		
		if option == "Login":
				
			

			if fielValues[0].lower() == username and fielValues[1] == password:
				easygui.msgbox("Logged in")

				breakornot = True
				break
			else:
					
				username = f.readline()
				username = username.strip()
				username = username.lower()
				#print "line = ///%s///" % username
				password = f.readline()	
				password = password.strip()
				#print "line = ///%s///" % password




	if breakornot == False:
		easygui.msgbox("Wrong username or password ")
	f.close()
