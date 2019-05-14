def odd_list(numlist):
    for num in numlist:
        if num % 2 != 0:
            print(num)
        else:
            continue

list1 = list(range(1, 31))

odd_list(list1)

