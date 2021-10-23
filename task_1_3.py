num = -1
while num < 235:
    num += 1
    num_end = num % 10
    if num_end == 0 or num == 11 or num == 12 or num == 13 or num == 14 or num_end == 5 or num_end == 6 or num_end == 7 or num_end == 8 or num_end == 9:
        print(str(num)+" процентов")
    elif num_end == 1:
        print(str(num)+" процент")
    elif num_end == 2 or num_end == 3 or num_end == 4:
        print(str(num) + " процентa")