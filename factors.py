Number = raw_input("Please enter a number.")
Number = float(Number)
Factors = []

Number_while_operation = Number + 1
x = 1

while x < Number_while_operation:
	
	if Number % x == 0:
		Factors.append(x)
	x += 1

print Factors

no_of_factors = len(Factors)

if no_of_factors == 2:
	print "Prime"
elif no_of_factors == 1:
	print "Special"
elif no_of_factors  == 0:
	print "Special"
else:
	print "Composite"