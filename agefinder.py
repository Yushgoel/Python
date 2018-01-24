
from datetime import datetime

now = datetime.now()
print now

date_of_birth = raw_input("Please enter your date of birth in DD-MM-YYYY.")
#date_of_birth = int(date_of_birth)

birth_year = date_of_birth.year
current_year = now.year


age = current_year - birth_year

print "age = " + age

