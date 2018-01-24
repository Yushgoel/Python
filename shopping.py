print "Hello, There is a discount dependant on the amount of money you spend"
print "Between Rs.1 to 700 - 30percent off"
print "AboveRs.700 - 50percent off"

money_spent = raw_input("Please enter the amount of money spent.")

money_spent = int(money_spent)

if money_spent >= 701:
   dicounted_price = 0.5 * money_spent 
   print "Price after discount = " + str(dicounted_price)

else:
	dicountedd_price = 0.7 * money_spent
	print "Price after discount = " + str(dicountedd_price)