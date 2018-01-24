import easygui

option = easygui.buttonbox("Sign up or login" ,choices = ["Sign up", "Login"])
breakornot = False

fielValues = []
Fields = ["Username", "Password"]
msg = "Enter username and password to login"
title = "Login/Signup"
fielValues = easygui.multpasswordbox(msg,title,Fields)
password = ""
username = " "
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
	#print "line = ///%s///" % password
while len(username) != 0:
	if option == "Sign up":
		f.write(fielValues[0] + "\n")
		f.write(fielValues[1] + "\n")
	elif option == "Login":
			
		'''username = f.readline()
		username = username.strip()
		#print "line = ///%s///" % username
		password = f.readline()	
		password = password.strip()
		#print "line = ///%s///" % password'''

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
