def biggest_number(*numb):
    print max(numb)
    return max(numb)

def smallest_number(*numb):
    print min(numb)
    return min(numb)

def distance_from_zero(numb):
	print abs(numb)
	return abs(numb)

biggest_number(10, 20, 30, 40)
smallest_number(21, 12, 1, 2)
distance_from_zero(-200)