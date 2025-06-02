# x = 2.4
# k = 4
# x = 5.3
# k = 6

x = float(input())
k = int(input())

isSum = True

resultFinal = 0

for index in range(2, k + 1, 2):
    # print(f"Fator : {index}")

    factorFinal = 1
    for i in range(1, index + 1):
        factorFinal *= i - index - 1
        # print(f"Fator Atual {i}/{index}: {index - i}")

    # print(f"Resultado Fatorial: {factorFinal}")

    # print(f"Resultado da Elevação: {x ** index}")

    math = x ** index / factorFinal

    if(isSum):
        resultFinal += math
    else: 
        resultFinal -= math

    isSum = not isSum

resultFinal = 1 - resultFinal

print(f"{resultFinal:.4f}")