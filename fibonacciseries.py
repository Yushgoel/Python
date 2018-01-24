nterms = raw_input("Please enter a number.")
nterms = int(nterms)
n1 = 0
n2 = 1
count = 2

print 0
print 1

while count < nterms:
	nth = n1 + n2
	print(nth)
	n1 = n2
	n2 = nth
	count += 1