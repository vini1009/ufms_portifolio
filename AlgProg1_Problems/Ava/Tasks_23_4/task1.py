n = int(input())

if (n == 1):
    print(n)
    quit()

finalFactor = 1
for index in range (1, n + 1):
    currentValue = n - (index - 1)
    finalFactor *= currentValue

print(finalFactor)