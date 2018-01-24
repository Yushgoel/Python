num = raw_input("Please enter a number.")
num = int(num)
factorial = 1

if num < 2:
	answer = 1

else:
        while factorial <= num:
                if factorial == 1:
			answer = factorial * (factorial + 1)
			factorial += 2
                else:
			answer = answer * factorial
			factorial += 1

print answer
