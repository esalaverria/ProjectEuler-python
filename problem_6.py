sum_squares = 0

sum = 0

for i in range(1, 101):
    sum_squares += i**2

for i in range(1, 101):
    sum += i

sum = sum**2

print sum - sum_squares
