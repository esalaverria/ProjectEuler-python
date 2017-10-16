x = 1
y = 0
num = 0
sum = 0
while num <= 4000000:
    num = x + y
    #print num
    if num % 2 == 0:
        sum += num
    y = x
    x = num

print sum
