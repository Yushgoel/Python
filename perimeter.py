length = raw_input("Please enter the length of the rectangle.")
length = float(length)
breadth = raw_input("Please enter the breadth of the rectangle.")
breadth = float(breadth)

def perimeter(l, b):
	fperimeter = l + b
	ftperimeter = 2 * fperimeter
	print ftperimeter 

perimeter(length, breadth)