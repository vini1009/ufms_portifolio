n = int(input())

counter = 0
lastNum = -1

for _ in range(1, n + 1):
    i = int(input())

    if (i > lastNum):
        counter += 1

        lastNum = i

        counter = 0

    counter += 1