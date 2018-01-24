def digit_sum(n):
	if n == 0:
		print "Please enter a positive number"
	else:
		n = str(n)
		counter = 0
		for item in n:
			if counter == 0:
				total = int(item)
			else:
				total = total + int(item)
				print total
			counter = counter + 1

n = raw_input("Please enter a number")
n = int(n)
digit_sum(n)