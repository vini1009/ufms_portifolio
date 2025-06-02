
""" 

Conveter Binário para deciomal

Raciocínio:
Pegue cada dígito do número binário.
Multiplique o dígito pela potência de 2 correspondente à sua posição.
Some todos os resultados.

"""

n = int(input())

decimal = 0
base = 1  # 2^0
while n > 0:
    ultimo_digito = n % 10 # Obtem o último dígito
    decimal += ultimo_digito * base # Obtem o decimal através do último dígito elevado a potência da base
    base *= 2 # Eleva a base a 2
    n = n // 10

print(decimal)