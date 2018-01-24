exponent = raw_input("Please enter the exponent.")
exponent = int(exponent)
num = 1
exponent_plus_one = exponent + 1

while num <= 10:
	ctr = 1
	product = num

	while ctr <= exponent:
		product = product * num
		ctr = ctr + 1
        print product
	num = num + 1

