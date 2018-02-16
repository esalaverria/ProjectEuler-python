
num = 1
i = 1
iterate = True
while iterate:
    while iterate:
        print("num: {0}, i: {1}".format(num, i))
        if num % i == 0:
            i += 1
        else:
            iterate = False

    if i > 20:
        iterate = False
    else:
        num += 1
        i = 1
        iterate = True

print(num)