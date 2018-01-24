Ayush_math = raw_input("Please enter Ayush's math marks.")
Ayush_math = int(Ayush_math)
Ayush_science = raw_input("Please enter Ayush's science marks.")
Ayush_science = int(Ayush_science)
Ayush_english = raw_input("Please enter Ayush's science marks.")
Ayush_english = int(Ayush_english)
Ayush_sum = Ayush_english + Ayush_science + Ayush_math

Mrinal_math = raw_input("Please enter Mrinal's math marks.")
Mrinal_math = int(Mrinal_math)
Mrinal_science = raw_input("Please enter Mrinal's science marks.")
Mrinal_science = int(Mrinal_science)
Mrinal_english = raw_input("Please enter Mrinal's english marks.")
Mrinal_english = int(Mrinal_english)
Mrinal_sum = Mrinal_english + Mrinal_science + Mrinal_math

Pranav_math = raw_input("Please enter Pranav's math marks.")
Pranav_math = int(Pranav_math)
Pranav_science = raw_input("Please enter Pranav's science marks.")
Pranav_science = int(Pranav_science)
Pranav_english = raw_input("Please enter Pranav's science marks.")
Pranav_english = int(Pranav_english)
Pranav_sum = Pranav_english + Pranav_science + Pranav_math

Siddhant_math = raw_input("Please enter Siddhant's math marks.")
Siddhant_math = int(Siddhant_math)
Siddhant_science = raw_input("Please enter Siddhant's science marks.")
Siddhant_science = int(Siddhant_science)
Siddhant_english = raw_input("Please enter Siddhant's science marks.")
Siddhant_english = int(Siddhant_english)
Siddhant_sum = Siddhant_science + Siddhant_english + Siddhant_math

Sum_list = [Ayush_sum, Mrinal_sum, Pranav_sum, Siddhant_sum]

for item in Sum_list:
	print item
	partpercent = item / 150
	percent = partpercent * 100
	print str(percent) + "%"

highest = 0

for item in Sum_list:
	if item > highest:
		highest = item

print "Highest: %s" % highest