number = raw_input("Please enter a positive number.")
number = float(number)
remainder = number % 2.0

if remainder == 0:
	print "Even"

else:
	print "Odd"