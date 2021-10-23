counter = 0
while counter < 1000:
    counter += 1
    if counter % 2 == 1:
        new_counter = counter**3
        degree = counter**3
        sum = 0
        while new_counter != 0:
            remainder = new_counter % 10
            sum += remainder
            new_counter //= 10
        if sum % 7 == 0:
            print(str(counter) + "^3: " + str(degree) + " sum: " + str(counter) + "[" + str(sum) + "]")
    else:
        continue