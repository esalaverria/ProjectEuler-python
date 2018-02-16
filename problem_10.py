import time
start = time.time()

sum = 0

def isPrime(num):
    limit = int(num**0.5) + 1

    if num == 1 or num == 2:
        return True

    for i in range(2, limit):
        if num % i == 0:
            return False

    return True


for i in xrange(2, 2000000):
    if isPrime(i):
        sum += i

print('Time: {:.5f} seconds'.format(time.time()-start))
print(sum)