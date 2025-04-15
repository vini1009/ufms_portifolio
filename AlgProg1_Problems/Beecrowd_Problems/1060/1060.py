# Números pares

i = 1
positiveCount = 0

while (i <= 6):
    value_input = float(input())
    if (value_input > 0):
        positiveCount += 1
    i += 1

print(f"{positiveCount} valores positivos")