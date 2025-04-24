a, b, c = map(float, input().split())

x = a
y = b
z = c

if a >= b and a >= c:
    if b >= c:
        first = a
        second = b
        third = c
    else:
        first = a
        second = c
        third = b
elif b >= a and b >= c:
    if a >= c:
        first = b
        second = a
        third = c
    else:
        first = b
        second = c
        third = a
else:
    if a >= b:
        first = c
        second = a
        third = b
    else:
        first = c
        second = b
        third = a

# print(f"{first} {second} {third}")

a = first
b = second
c = third

if (a >= (b + c)):
    print('NAO FORMA TRIANGULO')
elif ((a ** 2) == ((b ** 2) + (c ** 2))):
    print('TIANGULO RETANGULO')
elif ((a ** 2) > ((b ** 2) + (c ** 2))):
    print('TRIANGULO OBTUSANGULO')
elif ((a ** 2) < ((b ** 2) + (c ** 2))):
    print('TRIANGULO ACUTANGULO')
elif ()