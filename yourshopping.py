money_paid = raw_input("Please enter the amount of money spent.")
money_paid = float(money_paid)
discount = raw_input("Please enter the discount percent.")
discount = float(discount)
dis = (100.0 - discount) / 100.0

def discount_money (money, diss):

	after_discount_price = diss * money

	return after_discount_price; 

amount = discount_money(money_paid, dis)
print amount
