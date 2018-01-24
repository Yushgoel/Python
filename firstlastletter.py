string = raw_input("Please enter a string ")
whilel = len(string) - 1
print whilel
count = 0
answer = []
for i in string:
	if count == 0 or count == whilel:
		answer.append(i)
		print "error"
	count += 1
	print "count %s" % (count)
print answer