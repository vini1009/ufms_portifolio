n = int(input())

currentNum = n

counter = 0

while currentNum > 0:
    currentNum = currentNum // 10
    counter += 1

print(counter)