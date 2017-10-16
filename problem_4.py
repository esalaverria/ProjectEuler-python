
limit = 999
prod = 0
maxProd = 0
maxi = 0
maxj = 0
for i in range(1, limit + 1):
    for j in range(1, limit + 1):
        prod = i * j
        if str(prod) == str(prod)[::-1]:
            if prod > maxProd:
                maxProd = prod
                maxi = i
                maxj = j

print maxProd
print "{i} x {j}".format(i=maxi, j=maxj)
