#wierd concept, let me explain-
#highest sum of list :
#list = 0, 2, -4, 1
#hihest sum of consecutive numbers
#highest sum is 2
range1 = int(raw_input("How many numbers in list? "))
list1 = []
for i in range(0, range1):
    number = int(raw_input("Please enter number "))
    list1.append(number)
ctr = 0
for i in list1:
    if i < 0:
        ctr += 1
if ctr == len(list1) - 1:
    print max(list1)
else:
    index2 = 0
    highest_sum = 0
    sum1 = 0
    index1 = 0
    while index1 < len(list1):
        sum1 = list1[index1]
        index2 = index1 + 1
        if index1 == 0:

            highest_sum = sum1
        while index2 < len(list1):
            if sum1 + list1[index2] >= sum1:
                sum1 = sum1 + list1[index2]
            else:
                break;
            print "index2 %s" % index2
            index2 += 1
        if sum1 > highest_sum:
            highest_sum = sum1
        print "sum %s" % sum1
        print "highest sum %s" % highest_sum
        index1 += 1
        print "index1 %s" % index1
    print highest_sum
