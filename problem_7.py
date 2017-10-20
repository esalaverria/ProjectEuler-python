def isPrime(num):
    limit = int(num**0.5) + 1

    if num == 1 or num == 2:
        return True

    for i in range(2, limit):
        if num % i == 0:
            return False

    return True

counter = 0
num = 0
while counter <= 10001:
    num += 1
    if isPrime(num):
        counter += 1

print num
