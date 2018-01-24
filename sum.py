def digit_sum(n):
    x = str(n)
    counter = 0
    for item in n:
        if counter == 0:
            total = item
        else total += item
        return int(total)