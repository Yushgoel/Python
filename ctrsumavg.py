n = raw_input("How many numbers do you want to enter?")
n = int(n)

count = 0
sums = 0

while count < n:
	num = raw_input("Please enter a number.")
	num = int(num)
	sums = sums + num
	count = count + 1

avg = sums / n

print sums
print avg