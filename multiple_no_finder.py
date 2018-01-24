number = int(raw_input("Please enter a number "))
divisor = int(raw_input("Please enter the divisor "))

if number % divisor == 0:
	print " %s is divisible by %s" % (number, divisor)
else:
	print " %s is not divisible by %s" % (number, divisor)