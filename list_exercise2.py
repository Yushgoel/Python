list1 = [2, 2, 4, 6, 7, 8, 7, 4, 8, 6]
final_list = []
index_counter = 0

for item in list1:
	if item in final_list:
		print "%s item found" % item

	else:
		print "%s item not found" % item
		final_list.append(item)
	#if final_list.index(item) < 0:
	#	final_list.append(item)
	#else:
	#	list1.pop(index_counter)
	index_counter += 1

print final_list