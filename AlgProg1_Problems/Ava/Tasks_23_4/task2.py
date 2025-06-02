n = int(input())

if n == 0:
    print(0)
    exit()

divisor = 1
while divisor * 10 <= n:
    divisor *= 10

resultado = 0

while divisor > 0:
    digito = (n // divisor) % 10
    if digito % 2 == 0:
        resultado = resultado * 10 + digito
    divisor //= 10

print(resultado)
