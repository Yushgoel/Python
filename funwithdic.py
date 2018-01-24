English_m = {
	"Ayush" : 50,
	"Mrinal" : 48,
	"Siddhant" : 47,
	"Akshita" : 10,
    "Pranav" : 49,
    "Vasco da Gama" : 11,
    "Krishnadevaraya" : 1,
    "Vellukutty" : 0,
    "Einstein": 13,
    "Jeevesh" : 1
}

Maths_m = {
	"Ayush" : 50,
	"Mrinal" : 48,
	"Siddhant" : 47,
	"Akshita" : 48,
    "Pranav" : 49,
    "Vasco da Gama" : 11,
    "Krishnadevaraya" : 1,
    "Vellukutty" : 0,
    "Einstein": 13,
    "Jeevesh" : 1
}

Science_m = {
	"Ayush" : 50,
	"Mrinal" : 48,
	"Siddhant" : 47,
	"Akshita" : 9,
    "Pranav" : 49,
    "Vasco da Gama" : 11,
    "Krishnadevaraya" : 1,
    "Vellukutty" : 0,
    "Einstein": 13,
    "Jeevesh" : 1
}

def printmarks(dic):
	
	for key in dic:
		print key
                print "English marks: %s" % English_m[key]
		print "Maths marks: %s" % Maths_m[key]
		print "Science_m: %s" % Science_m[key]
		sum_m = English_m[key] + Science_m[key] + Maths_m[key]
		print "total %s" % sum_m
		print "------------------------------"
	

printmarks(English_m)

ctr = 0
for key in English_m:
	
	if ctr == 0:
		Largest = English_m[key]
		ctr = ctr + 1

	elif English_m[key] > Largest:
		Largest = English_m[key]


print "Largest = %s" % Largest

for key in English_m:
        fraction = sum_m / 150
        percent = fraction * 100
