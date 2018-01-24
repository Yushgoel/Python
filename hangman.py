from random import randint

f = open("hangman_list.txt", 'r') 
lines = f.readlines() 
word_list = []


for line in lines:
	word_list.append(line.strip())



f.close()

#self.lines = ["awesome", "discovery", "legend", "mythical", "historical", "competition", "frightful", "horrible", "pineapple"]
my_index = randint(0, 2)
my_word = word_list[my_index] #random word
guessed_input = []
player_input = 0
display = []
break_or_not = False
disp_old = "nothing"
ctr = 0
i = 0

def vowel(string):
	guess_display = []  #display for player
	for letter in string:
		if letter == "a" or letter == "A":
			guess_display.append(letter)

		elif letter == "e" or letter == "E":
			guess_display.append(letter)

		elif letter == "I" or letter == "i":
			guess_display.append(letter)

		elif letter == "o" or letter == "O":
			guess_display.append(letter)

		elif letter == "u" or letter == "U":
			guess_display.append(letter)

		else:
			guess_display.append("_")

	return guess_display;

#*****************************************************************

def game_over(d):
	counter = 0
	for i in d:
		if i == "_":
			counter += 1
	if counter == 0:
		print "you guessed my word !!!"
		return True;

#*****************************************************************

display = vowel(my_word)
disp = ' '.join(display)
print disp
#*****************************************************************
while i < 7:
	ctr = 0
	if i == 0 :
		print " "
	
	disp_old = disp
	print "chance %s" % (i + 1)
	player_input = raw_input("please enter an alphabet or word ")
	guessed_input.append(player_input)
	if len(player_input) > 1:
		if player_input == my_word:
			print "you guessed my word!!!" 
			break_or_not = True
			break
		else:
			print "wrong"
	else:
		for ini in my_word:
			if player_input == ini:
				display[ctr] = ini
				disp = ' '.join(display)
			ctr += 1
	break_or_not = game_over(display)
	if break_or_not == True:
		break
	if disp_old == disp:
		print " "
		i += 1
	print disp
	print " ".join(guessed_input)
	if i == 6:
		break_or_not = True


#*****************************************************************


if break_or_not == True:
	print " "
print "my word was %s" % my_word
print "Game over"
