string = raw_input("Please enter a word, letter or a sentence.")
ctr = 0

for letter in string:
	if letter == "a" or letter == "A":
		print letter
		ctr += 1
	elif letter == "e" or letter == "E":
		print letter
		ctr += 1
	elif letter == "I" or letter == "i":
		print letter
		ctr += 1
	elif letter == "o" or letter == "O":
		print letter
		ctr += 1
	elif letter == "u" or letter == "U":
		print letter
		ctr += 1


print ctr