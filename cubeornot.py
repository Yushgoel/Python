number = int(raw_input("Enter a number "))
count = 2
factors = []
prime_or_not = False
#while count < number:
#	if number % count == 0:
#		factors.append(count)
#	count += 1
#if len(factors) == 0:
#	print "%s is a prime number" % number

print factors
def prime(num):
	factor = 2
	factorlist = []
	while factor <= num:
		if num % factor == 0:
			factorlist.append(factor)
		factor += 1
	if len(factorlist) == 1:
		print "%s is a prime number" % num
		return True;
	else:
		print "not a prime number"
		return False;

while count < number:
	if count ** 3 == number:
		print "%s is a perfect cube. it's cube root is %s" % (number, count)
		break
	count += 1
