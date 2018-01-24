
operation = raw_input("Choose operator, \n1. add(+) \n2. subtract(-) \n3. divide(/) \n4. muliply(*) \n5. percentage(%) \n6. power(**) \nEnter the option number. ")
operation = int(operation)
operation_list = [1, 2, 3, 4, 5, 6]

if operation not in operation_list:
	print "invalid choice."
else:
	first_number = raw_input("please enter first number. ")
	first_number = float(first_number)

	second_number = raw_input("please enter second number. ")
	second_number = float(second_number)


	if operation == 1:
		print  " %s + %s" % (first_number, second_number)  + " = %s" % (first_number + second_number)
	elif operation == 2:
		print " %s - %s" % (first_number, second_number) + " = %s" % (first_number - second_number)
	elif operation == 3:
		print " %s / %s" % (first_number, second_number) + " = %s" % (first_number / second_number)
	elif operation == 4:
		print " %s * %s" % (first_number, second_number) + " = %s" % (first_number * second_number)
	elif operation == 5:
		print " %s percent of %s" % (second_number, first_number) + " = %s" % ((second_number / 100) * first_number)
	elif operation == 6:
		print " %s ** %s" % (first_number, second_number) + " = %s" % (first_number ** second_number)
