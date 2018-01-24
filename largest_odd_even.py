lists = [1, 2, 3, 4, 5, 6, 7, 8, 9]
len_lists = len(lists)
count = 0
largest_even = 0
largest_odd = 1
while count < len_lists:
	for i in lists:
		if i % 2 == 0:
			if i > largest_even:
				largest_even = i
		else:
			if i > largest_odd:
				largest_odd = i
	count += 1


print largest_even
print largest_odd