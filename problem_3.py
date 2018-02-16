
def isPrime(num):
    limit = int(num**0.5)

    if num == 1 or num == 2:
        return True

    for i in range(2, limit):
        if num % i == 0:
            return False

    return True

n = 600851475143
limit = int(n**0.5)
lastFactor = 1

for i in range(3, limit, 2):
    if isPrime(i) and n % i == 0:
        lastFactor = i

print(lastFactor)

