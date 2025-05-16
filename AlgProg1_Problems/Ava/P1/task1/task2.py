n = int(input())

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

if (n == 0 or n == 1):
    print(n)
else:
    a = 0
    b = 1

    for _ in range(2, n + 1):
        fib = a + b
        # print(f"{fib}")

        a = b
        b = fib

    print(fib)


# p = 1
# p = 2

#def teste(a, b)
# return p