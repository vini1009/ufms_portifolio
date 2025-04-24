a, b, c = map(int, input().split())

x = a
y = b
z = c

if a <= b and a <= c:
    if b <= c:
        first = a
        second = b
        third = c
    else:
        first = a
        second = c
        third = b
elif b <= a and b <= c:
    if a <= c:
        first = b
        second = a
        third = c
    else:
        first = b
        second = c
        third = a
else:
    if a <= b:
        first = c
        second = a
        third = b
    else:
        first = c
        second = b
        third = a

print(first)
print(second)
print(third)
print()
print(x)
print(y)
print(z)
