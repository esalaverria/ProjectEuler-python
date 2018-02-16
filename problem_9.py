import time
start = time.time()

found = False

for a in range(1, 1000):
    if found:
        break
    for b in range(a+1, 1000):
        c = a**2 + b**2
        c = c**0.5
        if a + b + c == 1000:
            print('Time: {:.5f} seconds'.format(time.time()-start))
            print('a: {} b: {} c: {}'.format(a, b, c))
            print(a + b + c)
            print(a * b * c)
            found = True
            break

