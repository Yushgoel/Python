num1 = int(raw_input("enter a number "))
num2 = int(raw_input("enter a number "))
ctr = 0
answer = 0

while ctr < min(num2, num1):
	answer += num1
	ctr += 1

print answer
