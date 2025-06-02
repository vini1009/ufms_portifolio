'''

#### Converter Decimal para Binário ####
Dividir por 2, obter o quociente (resultado da divisão)
e Dividir sucessivamente até que o quociente seja zero
-- Obter o Resto da divisão sempre, esse é o resultado binário

'''

i = int(input())

if i == 0:
    print(0)
else:
    # descobrir a maior potência de 2 menor ou igual a i
    power = 1
    while power <= i:
        power = power * 2
    power = power // 2

    currentValue = i
    while power > 0:
        bit = currentValue // power
        print(bit, end="")
        currentValue = currentValue - bit * power
        power = power // 2


