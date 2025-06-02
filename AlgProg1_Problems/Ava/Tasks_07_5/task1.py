n = int(input())

if n == 0:
    print(0)
else:
    result = 0
    multiplier = 1

    while n > 0:
        rest = n % 3
        result += rest * multiplier
        multiplier *= 10
        n = n // 3

    print(result)
