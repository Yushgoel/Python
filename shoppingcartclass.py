class Shoppingcart(object):
	cart = {}
	def __init__(self, price, item):
		self.price = price
		self.item = item
		cart[item][price]
	print cart
rice = Shoppingcart("rice", 100)
