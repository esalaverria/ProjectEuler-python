numbers = open('problem_8_string.txt')
adjacents = []
subline = ''

limit = 13
num = 1
maxnum = 0
for line in numbers:
    line = line.replace('\n', '')

    for i in range(0, len(line)):

        if (i + limit) - 1 <= (len(line) - 1):

            for j in range(i, i + limit):
                num *= int(line[j])

            if num > maxnum:
                adjacents = line[i:i+limit]
                subline = line
                maxnum = num

        num = 1

print maxnum
print adjacents
print subline

