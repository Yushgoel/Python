largestnum = -1
question = []
answerarray = []
answer = 0
isCorrectInput = False
try:
	numoftime = int(raw_input("How many numbers? "))
	isCorrectInput = True

except ValueError:
	print "error, enter valid numbers"	

if isCorrectInput:
	if numoftime <= 0:
		print "error as you can enter only a positive number of digits."
	else:
		ctr = 0
		n = 10 ** (numoftime - 1)

		for i in range(numoftime):
			i = int(raw_input("enter number "))
			question.append(i)

		while ctr < numoftime:
			largestnum = 0
			for i in question:
				if largestnum < i:
					largestnum = i
			answerarray.append(largestnum)
			question.remove(largestnum)
			print question
			ctr += 1

		print answerarray
		for i in answerarray:
			answer = answer + (i * n)
			n = n / 10

		print answer
