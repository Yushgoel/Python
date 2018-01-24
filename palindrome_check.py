input_str = raw_input("PLEASE enter a word ")
ctr = 0
rctr = len(input_str) - 1
char = ""
list1 = []

for i in reversed(input_str):
	list1.append(i)


if "".join(list1) == input_str:
	print "palindrome"

input_str = "".join(list1)
print input_str[0]
while ctr < len(input_str):
	char = input_str[ctr]
	input_str[ctr] = input_str[rctr]
	input_str[rctr] = char
	ctr += 1
	rctr -= 1
print input_str
input_str[0] = "s"
print input_str
