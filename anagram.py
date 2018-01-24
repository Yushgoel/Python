l1 = []
l2 = []
s1 = raw_input("PLEASE enter a word ")
s2 = raw_input("PLEASE enter a word ")

for i in s1:
	l1.append(i)
for i in s2:
	l2.append(i)


for li1 in l1:
	ctr = 0
	for li2 in l2:
		
		if li1 == li2:
			l2[ctr] = 0
		ctr += 1

ctr = 0
for i in l2:
	if i == 0:
		ctr += 1

if ctr == len(l2):
	print "anagram"