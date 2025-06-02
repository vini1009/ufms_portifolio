x = float(input())
n = int(input())

# x = 1.0
# n = 4

resultFinal = 0

for index in range(1, n + 1):

    factor = 1
   
    for i in range(1, index + 1):
        currentValue = index - (i - 1)
        factor *= currentValue

    resultFinal += x ** index / factor
    # print (f"Fator de {index}: {factor}")

resultFinal = x ** 0 + resultFinal

print(f"{resultFinal:.4f}")