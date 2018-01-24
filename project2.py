science = raw_input("Please enter science marks")
science = int(science)
maths = raw_input("Please enter maths marks")
maths = int(maths)
english = raw_input("Please enter english marks")
english = int(english)

#this function will find sum of marks. 
def add(sub1, sub2, sub3):
	total = sub1 + sub2 + sub3
	return total;
	
def passing(totalm):
	if totalm > 50:
	   print "pass"
	else:
	 	print "fail";

answer = add(science, maths, english)
print answer
passing(answer)  
