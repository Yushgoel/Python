from random import randint
my_num = randint(0, 10)
print """Try and guess my number.
It is from 0 to 10"""
guess = int(raw_input("Please enter a number "))

chance = 1
while chance <= 3:
	
	if guess == my_num:
		print "You guessed my number."
		chance += 10
	else:
		print "chances left = %s" % (5 - (chance + 1))
		guess = int(raw_input("Wrong try again. "))
		chance += 1
		

if chance == 4:
	print "Sorry your chances are over."
	print my_num