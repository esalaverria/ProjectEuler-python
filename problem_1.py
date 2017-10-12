sum = 0
for i in range(1, 1000):
    resto3 = i % 3
    if resto3 == 0:
       sum += i
    else:
        resto5 = i % 5
        if resto5 == 0:
            sum += i


print sum