list1 = ["apple", "banana", "apple"]
answer = list1
list2 = []
print answer
print list1
ctr = 0
for i in list1:
	print i
	if len(list2) == 0:
		list2.append(i)
	
	else:
		for z in list2:
			if i == z:
				#answer.pop(ctr)
				print answer
				break
	
			else:
				list2.append(i)
	ctr += 1

print answer