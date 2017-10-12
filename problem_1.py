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

#Shorter solution

sum = 0
for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        sum += i

print sum